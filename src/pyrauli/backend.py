"""
Defines the Qiskit-compatible BackendV2 for the pyrauli simulator.
"""
import uuid
from typing import List, Tuple, Dict, Any, Union

import pyrauli
from .converters import from_qiskit
from .estimator import PyrauliEstimator

from qiskit.providers import BackendV2, JobV1, Options, JobStatus
from qiskit.result import Result
from qiskit.transpiler import Target
from qiskit.circuit import QuantumCircuit
from qiskit.circuit.library import HGate, CXGate, RZGate, Measure
from qiskit.quantum_info import SparsePauliOp


class PBackend(BackendV2):
    """
    A Qiskit BackendV2 that uses the pyrauli simulator.

    This backend integrates pyrauli's Pauli back-propagation engine into the
    Qiskit ecosystem, allowing it to be used as a target for Qiskit's transpiler
    and as a simulator for running quantum circuits.

    .. code-block:: python

        from qiskit.circuit import QuantumCircuit
        from qiskit.quantum_info import SparsePauliOp
        from pyrauli import PBackend

        # Create a Qiskit circuit
        qc = QuantumCircuit(2)
        qc.h(0)
        qc.cx(0, 1)

        # Define an observable and instantiate the backend
        obs = SparsePauliOp("ZI")
        backend = PBackend()

        # Run using the PUB (Primitive Unified Bloc) format
        job = backend.run([(qc, obs)])
        result = job.result()
        ev = result.results[0].data.evs[0]

        print(f"Expectation value from Qiskit backend: {ev}")

    """

    def __init__(self, num_qubits: int = 128, noise_model: pyrauli.NoiseModel = None, truncator: pyrauli.Truncator = pyrauli.NeverTruncator(), merge_policy: pyrauli.SchedulingPolicy = pyrauli.AlwaysAfterSplittingPolicy(), truncate_policy: pyrauli.SchedulingPolicy = pyrauli.AlwaysAfterSplittingPolicy(), **kwargs):
        """
        Initializes the PBackend.

        Args:
            num_qubits: The maximum number of qubits the backend supports.
            noise_model: A pyrauli.NoiseModel to apply to circuits run on this backend.
            truncator: A pyrauli.Truncator to apply to circuits.
            merge_policy: A merge pyrauli.SchedulingPolicy to apply to circuits.
            truncate_policy: A truncate pyrauli.SchedulingPolicy to apply to circuits.
            **kwargs: Additional arguments for the parent BackendV2 class.
        """
        super().__init__(name="pyrauli.PBackend", **kwargs)
        self._num_qubits = num_qubits
        self._noise_model = noise_model or pyrauli.NoiseModel()
        self._truncator = truncator or pyrauli.NeverTruncator()
        self._merge_policy = merge_policy or pyrauli.AlwaysAfterSplittingPolicy()
        self._truncate_policy = truncate_policy or pyrauli.AlwaysAfterSplittingPolicy()
        self._target = Target(description="Pyrauli Backend Target", num_qubits=num_qubits)

        # Define the basis gates for the target
        self._target.add_instruction(HGate(), {(i,): None for i in range(self._num_qubits)})
        self._target.add_instruction(
            CXGate(), {(i, j): None for i in range(self._num_qubits) for j in range(self._num_qubits) if i != j}
        )
        self._target.add_instruction(Measure(), {(i,): None for i in range(self._num_qubits)})
        self._target.add_instruction(RZGate, name='rz')

    @property
    def target(self) -> Target:
        """
        The Qiskit Target object for this backend, detailing supported gates and connectivity.
        """
        return self._target

    @property
    def max_circuits(self) -> int:
        """The maximum number of circuits that can be run in a single job."""
        return 1024

    @classmethod
    def _default_options(cls) -> Options:
        """Default options for the backend."""
        return Options()

    def run(self, run_input: Union[QuantumCircuit, List[QuantumCircuit]], **options) -> JobV1:
        """
        Run a circuit or a list of circuits on the backend.

        This backend uses a PyrauliEstimator to execute the circuits.

        Args:
            run_input: A QuantumCircuit or a list of them to run.
            **options: Runtime options for the execution. may include: "noise_model", "truncator", "merge_policy", "truncate_policy"

        Returns:
            A JobV1 object that represents the execution.
        """
        pyest = PyrauliEstimator(noise_model=self._noise_model, truncator=self._truncator, merge_policy=self._merge_policy, truncate_policy=self._truncate_policy)
        return pyest.run(run_input, **options)
