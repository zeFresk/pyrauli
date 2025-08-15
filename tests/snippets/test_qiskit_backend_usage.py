import pytest

# Skip this entire module if qiskit is not installed
qiskit = pytest.importorskip("qiskit", reason="Qiskit extra not installed")

from qiskit.circuit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from pyrauli import PBackend

def test_qiskit_backend_snippet():
    # [qiskit_backend_usage]
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
    ev = result[0].data.evs[0]

    print(f"Expectation value from Qiskit backend: {ev}")
    # [qiskit_backend_usage]
