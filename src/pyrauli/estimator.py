import uuid
import numpy as np
from concurrent.futures import ThreadPoolExecutor

from qiskit.primitives import BaseEstimatorV2
from qiskit.providers import BackendV2, JobV1, Options, JobStatus
from qiskit.result import Result
from qiskit.primitives.primitive_job import PrimitiveJob
from qiskit.primitives.containers import PubResult, PrimitiveResult, DataBin
from qiskit.quantum_info import SparsePauliOp

from . import Circuit, Observable, NoiseModel
from .converters import from_qiskit

class PyrauliEstimator(BaseEstimatorV2):
    """
    A Qiskit Estimator primitive that uses the pyrauli C++ simulator.
    """
    def __init__(self, noise_model: NoiseModel = None):
        super().__init__()
        self.name = "PyrauliEstimator"
        self._noise_model = noise_model or NoiseModel()
        self._executor = ThreadPoolExecutor(max_workers=1)


    def run(self, run_input, **options):
        pubs = run_input if isinstance(run_input, list) else [run_input]
        job = PJob(backend=self, job_id=str(uuid.uuid4()), fn=self._run_job, pubs=pubs)
        job.submit()
        return job

    def _run_job(self, job_id, pubs):
        results = []
        for pub in pubs:
            circuit, observables, parameter_values = self._unpack_pub(pub)

            bound_circuit = circuit.assign_parameters(parameter_values) if parameter_values else circuit
            pyrauli_circuit = from_qiskit(bound_circuit, noise_model=self._noise_model)
            exp_values = self._simulate_observables(pyrauli_circuit, observables)
            results.append({"success": True, "data": {"evs": exp_values}, "metadata": {}, 'shots': 1})
        return Result.from_dict({"job_id": job_id, "results": results, "success": True, "backend_name": self.name})

    def _simulate_observables(self, pyrauli_circuit, observables):
        exp_values = []
        for obs in observables:
                pyrauli_obs = from_qiskit(obs)
                final_observable = pyrauli_circuit.run(pyrauli_obs)
                exp_values.append(final_observable.expectation_value())
        return exp_values

    def _unpack_pub(self, pub):
        circuit, observables, params = (pub[0], pub[1], pub[2] if len(pub) > 2 else None)
        return circuit, observables if isinstance(observables, list) else [observables], params

class PJob(JobV1):
    """A JobV2-compliant class for the PBackend."""
    def __init__(self, backend, job_id, fn, pubs):
        super().__init__(backend, job_id)
        self._fn = fn
        self._pubs = pubs
        self._result = None
        self._status = JobStatus.INITIALIZING

    def submit(self):
        """Submit the job for execution."""
        self._status = JobStatus.RUNNING
        try:
            self._result = self._fn(self.job_id, self._pubs)
            self._status = JobStatus.DONE
        except Exception as e:
            self._status = JobStatus.ERROR
            raise e

    def result(self):
        """Return the result of the job."""
        return self._result.results if self._result is not None else None

    def status(self):
        """Return the status of the job."""
        return self._status

    def running(self):
        """Return whether the job is actively running."""
        return self._status == JobStatus.RUNNING

    def cancelled(self):
        """Return whether the job has been cancelled."""
        return self._status == JobStatus.CANCELLED

    def done(self):
        """Return whether the job has successfully run."""
        return self._status == JobStatus.DONE

    def in_final_state(self):
        """Return whether the job is in a final job state."""
        return self._status in {JobStatus.DONE, JobStatus.ERROR, JobStatus.CANCELLED}
