"""
Defines the Qiskit Estimator primitive for the pyrauli simulator.

This module contains the `PyrauliEstimator` class, which is a Qiskit `BaseEstimatorV2`
primitive, and the `PJob` class, which is a `JobV1`-compliant class for
managing simulation jobs.
"""
import uuid
import numpy as np
from typing import List, Tuple, Union, Optional, Any, Callable, Dict
from concurrent.futures import ThreadPoolExecutor

from qiskit import QuantumCircuit
from qiskit.primitives import BaseEstimatorV2
from qiskit.providers import BackendV2, JobV1, Options, JobStatus
from qiskit.result import Result
from qiskit.primitives.primitive_job import PrimitiveJob
from qiskit.primitives.containers import PubResult, PrimitiveResult, DataBin
from qiskit.quantum_info import SparsePauliOp
from qiskit.circuit import ParameterVector

from . import Circuit, Observable, NoiseModel, Truncator, NeverTruncator, SchedulingPolicy, AlwaysAfterSplittingPolicy, RuntimePolicy, default_batch_policy
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
    def __init__(self, 
                 noise_model: Optional[NoiseModel] = None, 
                 truncator: Truncator = NeverTruncator(), 
                 merge_policy: SchedulingPolicy = AlwaysAfterSplittingPolicy(), 
                 truncate_policy: SchedulingPolicy = AlwaysAfterSplittingPolicy(),
                 runtime: RuntimePolicy = default_batch_policy) -> None:
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
        self._runtime = runtime or default_batch_policy
        self._executor = ThreadPoolExecutor(max_workers=1)

    def run(self, run_input: Union[List[Tuple], Tuple], **options: Any) -> 'PJob':
        """
        Run a list of pubs (Primitive Unified Blocs) on the estimator.

        Args:
            run_input: A list of pubs, where each pub is a tuple of (circuit, observables, parameter_values). See qiskit documentation on PUBs
            **options: Additional circuit options: "noise_model", "truncator", 
                       "truncate_policy", "merge_policy".

        Returns:
            A PJob object that represents the asynchronous execution.
        """
        pubs = run_input if isinstance(run_input, list) else [run_input]
        job = PJob(backend=self, job_id=str(uuid.uuid4()), fn=self._run_job, pubs=pubs, options=options)
        job.submit()
        return job

    def _run_job(self, job_id: str, pubs: List[Tuple], **options: Any) -> Result:
        """
        The core simulation logic that is executed by the PJob.

        Args:
            job_id: The ID for the job.
            pubs: The list of pubs to execute.
            **options: Runtime options passed to the run method.

        Returns:
            A Qiskit Result object containing the simulation results.
        """
        nm = self._noise_model if "noise_model" not in options else options.get("noise_model")
        trunc = self._truncator if "truncator" not in options else options.get("truncator")
        trunc_pol = self._truncate_policy if "truncate_policy" not in options else options.get("truncate_policy")
        merge_pol = self._merge_policy if "merge_policy" not in options else options.get("merge_policy")
        runtime = self._runtime if "runtime" not in options else options.get("runtime")

        results = []
        for pub in pubs:
            circuit, observables, parameter_values = self._unpack_pub(pub)

            # Bind parameters if they exist
            bound_circuits = self._assign_parameters(circuit, parameter_values)
            
            # Convert to pyrauli objects and simulate
            pyrauli_circuits = [from_qiskit(bqc, noise_model=nm) for bqc in bound_circuits]
            for pyrauli_circuit in pyrauli_circuits:
                pyrauli_circuit.set_truncator(trunc)
                pyrauli_circuit.set_merge_policy(merge_pol)
                pyrauli_circuit.set_truncate_policy(trunc_pol)

            exp_values = self._simulate_observables(pyrauli_circuits, observables, runtime) 
            print(exp_values)
            evs = np.array(exp_values)
            print(evs)
            
            # Format the result for this pub
            results.append({"success": True, "data": {"evs": exp_values}, "metadata": {}, 'shots': 1})
            
        return Result.from_dict({"job_id": job_id, "results": results, "success": True, "backend_name": self.name})

    def _simulate_observables(self, 
                              pyrauli_circuits: List[Circuit], 
                              observables: Union[List[List[SparsePauliOp]], List[SparsePauliOp]], 
                              runtime: RuntimePolicy) -> np.ndarray:
        """
        Simulates a list of observables for a given pyrauli circuit.
        """
        if not observables:
            return np.array([])

        nb_obs_arr = len(observables)
        nb_qcs = len(pyrauli_circuits)

        long = False
        if (isinstance(observables, np.ndarray) and observables.ndim == 2) or (isinstance(observables[0], list)):
            observables = [o for obs in observables for o in obs]
            long = True

        pobs = [from_qiskit(o, reverse=True) for o in observables]

        results_per_circuit = [
            pqc.expectation_value(pobs, runtime=runtime) for pqc in pyrauli_circuits
        ]

        matrix_circ_obs = np.array(results_per_circuit)
        matrix_obs_circ = matrix_circ_obs.T

        if long:
            return np.atleast_1d(np.squeeze(matrix_obs_circ.flatten().reshape(nb_obs_arr, nb_qcs)))
        else:
            return matrix_obs_circ.flatten()

    def _unpack_pub(self, pub: Tuple) -> Tuple[QuantumCircuit, List[SparsePauliOp], Optional[Any]]:
        """
        Unpacks a pub into its components, ensuring observables are always a list.
        """
        circuit, observables, params = (pub[0], pub[1], pub[2] if len(pub) > 2 else None)
        return circuit, observables if isinstance(observables, list) else [observables], params

    def _assign_parameters(self, circuit: QuantumCircuit, params: Optional[Any]) -> List[QuantumCircuit]:
        """
        Assigns parameter values to a circuit.

        This method handles different shapes for the parameter values, including
        no parameters, a single set of parameters, or multiple sets for
        parameter sweeping.

        Args:
            circuit: The circuit with unbound parameters.
            params: The parameter values to bind. Can be a 1D array for a single
                binding or a 2D array for multiple bindings.

        Returns:
            A list of circuits with bound parameters.
        """
        if params is None:
            return [circuit]
        elif (hasattr(params, 'ndim') and params.ndim == 2) or ((isinstance(params, list) or hasattr(params, 'ndim')) and len(params) > 0 and isinstance(params[0], (list, tuple, dict, ParameterVector))):
            return [circuit.assign_parameters(e) for e in params]
        else:
            return [circuit.assign_parameters(params)]

class PJob(JobV1):
    """
    A JobV1-compliant class for handling jobs from PBackend and PyrauliEstimator.
    
    This class wraps the execution of the simulation in a manner consistent
    with Qiskit's job management system.
    """
    def __init__(self, 
                 backend: BackendV2, 
                 job_id: str, 
                 fn: Callable[..., Result], 
                 pubs: List[Tuple], 
                 **options: Any) -> None:
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
        self._result: Optional[Result] = None
        self._status = JobStatus.INITIALIZING
        self._options = options

    def submit(self) -> None:
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

    def result(self) -> Optional[List[Result]]:
        """Return the result of the job."""
        return self._result.results if self._result is not None else None

    def status(self) -> JobStatus:
        """Return the status of the job."""
        return self._status

    def running(self) -> bool:
        """
        Return whether the job is actively running.

        Returns:
            True if the job's status is 'RUNNING', False otherwise.
        """
        return self._status == JobStatus.RUNNING

    def cancelled(self) -> bool:
        """
        Return whether the job has been cancelled.

        Returns:
            True if the job's status is 'CANCELLED', False otherwise.
        """
        return self._status == JobStatus.CANCELLED

    def done(self) -> bool:
        """
        Return whether the job has successfully run.

        Returns:
            True if the job's status is 'DONE', False otherwise.
        """
        return self._status == JobStatus.DONE

    def in_final_state(self) -> bool:
        """
        Return whether the job is in a final job state.

        Returns:
            True if the job is in a final state (DONE, ERROR, or
            CANCELLED), False otherwise.
        """
        return self._status in {JobStatus.DONE, JobStatus.ERROR, JobStatus.CANCELLED}
