"""
Defines the Qiskit Estimator primitive for the pyrauli simulator.

This module contains the `PyrauliEstimator` class, which is a Qiskit `BaseEstimatorV2`
primitive, and the `PJob` class, which is a `JobV1`-compliant class for
managing simulation jobs.
"""
import uuid
import numpy as np
from typing import List, Tuple, Union
from concurrent.futures import ThreadPoolExecutor

from qiskit.primitives import BaseEstimatorV2
from qiskit.providers import BackendV2, JobV1, Options, JobStatus
from qiskit.result import Result
from qiskit.primitives.primitive_job import PrimitiveJob
from qiskit.primitives.containers import PubResult, PrimitiveResult, DataBin
from qiskit.quantum_info import SparsePauliOp

from . import Circuit, Observable, NoiseModel, Truncator, NeverTruncator, SchedulingPolicy, AlwaysAfterSplittingPolicy
from .converters import from_qiskit

class PyrauliEstimator(BaseEstimatorV2):
    """
    A Qiskit Estimator primitive that uses the pyrauli C++ simulator.

    This estimator calculates the expectation values of observables for given
    quantum circuits, leveraging the high-performance Pauli back-propagation
    engine of pyrauli.

    .. code-block:: python

        from qiskit.circuit import QuantumCircuit
        from qiskit.quantum_info import SparsePauliOp
        from pyrauli import PyrauliEstimator

        estimator = PyrauliEstimator()
        qc = QuantumCircuit(1)
        qc.h(0)
        obs = SparsePauliOp("Z") # EV of Z on |+> state is 0

        job = estimator.run([(qc, obs)])
        result = job.result()
        print(result[0].data.evs[0])
    """
    def __init__(self, noise_model: NoiseModel = None, truncator: Truncator = NeverTruncator(), merge_policy: SchedulingPolicy = AlwaysAfterSplittingPolicy(), truncate_policy: SchedulingPolicy = AlwaysAfterSplittingPolicy()):
        """
        Initializes the PyrauliEstimator.

        Args:
            noise_model: A pyrauli.NoiseModel to apply during simulation.
            truncator: A pyrauli.Truncator to apply to circuits.
            merge_policy: A merge pyrauli.SchedulingPolicy to apply to circuits.
            truncate_policy: A truncate pyrauli.SchedulingPolicy to apply to circuits.
        """
        super().__init__()
        self.name = "PyrauliEstimator"
        self._noise_model = noise_model or NoiseModel()
        self._truncator = truncator or NeverTruncator()
        self._merge_policy = merge_policy or AlwaysAfterSplittingPolicy()
        self._truncate_policy = truncate_policy or AlwaysAfterSplittingPolicy()

        self._executor = ThreadPoolExecutor(max_workers=1)


    def run(self, run_input: List[Tuple], **options) -> 'PJob':
        """
        Run a list of pubs (Primitive Unified Blocs) on the estimator.

        Args:
            run_input: A list of pubs, where each pub is a tuple of
                      (circuit, observables, parameter_values).
            **options: Additional circuit options: "noise_model", "truncator", "truncate_policy", "merge_policy".

        Returns:
            A PJob object that represents the asynchronous execution.
        """
        pubs = run_input if isinstance(run_input, list) else [run_input]
        job = PJob(backend=self, job_id=str(uuid.uuid4()), fn=self._run_job, pubs=pubs, options=options)
        job.submit()
        return job

    def _run_job(self, job_id: str, pubs: List[Tuple], **options) -> Result:
        """
        The core simulation logic that is executed by the PJob.

        Args:
            job_id: The ID for the job.
            pubs: The list of pubs to execute.

        Returns:
            A Qiskit Result object containing the simulation results.
        """
        nm = self._noise_model if "noise_model" not in options else options.get("noise_model")
        trunc = self._truncator if "truncator" not in options else options.get("truncator")
        trunc_pol = self._truncate_policy if "truncate_policy" not in options else options.get("truncate_policy")
        merge_pol = self._merge_policy if "merge_policy" not in options else options.get("merge_policy")
        print(nm, self._noise_model)

        results = []
        for pub in pubs:
            circuit, observables, parameter_values = self._unpack_pub(pub)

            # Bind parameters if they exist
            bound_circuit = circuit.assign_parameters(parameter_values) if parameter_values is not None else circuit
            
            # Convert to pyrauli objects and simulate
            pyrauli_circuit = from_qiskit(bound_circuit, noise_model=nm)
            pyrauli_circuit.set_truncator(trunc)
            pyrauli_circuit.set_merge_policy(merge_pol)
            pyrauli_circuit.set_truncate_policy(trunc_pol)
            exp_values = self._simulate_observables(pyrauli_circuit, observables)
            
            # Format the result for this pub
            results.append({"success": True, "data": {"evs": exp_values}, "metadata": {}, 'shots': 1})
            
        return Result.from_dict({"job_id": job_id, "results": results, "success": True, "backend_name": self.name})

    def _simulate_observables(self, pyrauli_circuit: Circuit, observables: List[SparsePauliOp]) -> List[float]:
        """
        Simulates a list of observables for a given pyrauli circuit.
        """
        exp_values = []
        for obs in observables:
                pyrauli_obs = from_qiskit(obs, reverse=True)
                final_observable = pyrauli_circuit.run(pyrauli_obs)
                exp_values.append(final_observable.expectation_value())
        return exp_values

    def _unpack_pub(self, pub: Tuple) -> Tuple:
        """
        Unpacks a pub into its components, ensuring observables are always a list.
        """
        circuit, observables, params = (pub[0], pub[1], pub[2] if len(pub) > 2 else None)
        return circuit, observables if isinstance(observables, list) else [observables], params

class PJob(JobV1):
    """
    A JobV1-compliant class for handling jobs from PBackend and PyrauliEstimator.
    
    This class wraps the execution of the simulation in a manner consistent
    with Qiskit's job management system.
    """
    def __init__(self, backend, job_id, fn, pubs, **options):
        """
        Initializes the PJob.

        Args:
            backend: The backend that this job belongs to.
            job_id: The unique ID for this job.
            fn: The function to execute for the job (typically `_run_job`).
            pubs: The list of pubs to be processed by the job.
            **options: More options to pass to pyrauli.Circuit
        """
        super().__init__(backend, job_id)
        self._fn = fn
        self._pubs = pubs
        self._result = None
        self._status = JobStatus.INITIALIZING
        self._options = options

    def submit(self):
        """
        Submit the job for execution.
        
        This implementation runs the job synchronously.
        """
        self._status = JobStatus.RUNNING
        try:
            self._result = self._fn(self.job_id(), self._pubs, **self._options.get("options"))
            self._status = JobStatus.DONE
        except Exception as e:
            self._status = JobStatus.ERROR
            raise e

    def result(self) -> Result:
        """Return the result of the job."""
        return self._result.results if self._result is not None else None

    def status(self) -> JobStatus:
        """Return the status of the job."""
        return self._status

    def running(self) -> bool:
        """Return whether the job is actively running."""
        return self._status == JobStatus.RUNNING

    def cancelled(self) -> bool:
        """Return whether the job has been cancelled."""
        return self._status == JobStatus.CANCELLED

    def done(self) -> bool:
        """Return whether the job has successfully run."""
        return self._status == JobStatus.DONE

    def in_final_state(self) -> bool:
        """Return whether the job is in a final job state."""
        return self._status in {JobStatus.DONE, JobStatus.ERROR, JobStatus.CANCELLED}
