import uuid
import inspect
from pyrauli.estimator import PyrauliEstimator
from qiskit.providers import BackendV2, JobV1, Options, JobStatus
from qiskit.result import Result
from qiskit.transpiler import Target, InstructionProperties
from qiskit.circuit.library import HGate, CXGate, RZGate, Measure
from qiskit.quantum_info import SparsePauliOp

import pyrauli
from .converters import from_qiskit

class PBackend(BackendV2):
    """
    A Qiskit backend that uses the pyrauli simulator.
    """
    def __init__(self, num_qubits = 128, noise_model: pyrauli.NoiseModel = None, **kwargs):
        super().__init__(name="pyrauli.PBackend", **kwargs)
        self._num_qubits = num_qubits
        self._noise_model = noise_model or pyrauli.NoiseModel()
        self._target = Target(description="Pyrauli Backend Target", num_qubits=num_qubits)
        self._target.add_instruction(HGate(), {(i,): None for i in range(self._num_qubits)})
        self._target.add_instruction(CXGate(), {(i, j): None for i in range(self._num_qubits) for j in range(self._num_qubits) if i != j})
        self._target.add_instruction(Measure(), {(i,): None for i in range(self._num_qubits)})
        self._target.add_instruction(RZGate, name='rz')

    @property
    def target(self): return self._target
    @property
    def max_circuits(self): return 1024
    @classmethod
    def _default_options(cls): return Options()

    def run(self, run_input, **options):
        pyest = PyrauliEstimator(noise_model=self._noise_model)
        return pyest.run(run_input, **options)
