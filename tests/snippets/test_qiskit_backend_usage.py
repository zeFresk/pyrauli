import pytest

# Skip this entire module if qiskit is not installed
qiskit = pytest.importorskip("qiskit", reason="Qiskit extra not installed")

from qiskit.circuit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from pyrauli import PBackend, NoiseModel, QGate, UnitalNoise

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


def test_backend_noise1():
    # [backend_noise]
    # Define a default noise model
    p = 0.1
    default_noise = NoiseModel()
    default_noise.add_unital_noise_on_gate(QGate.H, UnitalNoise.Depolarizing, p)

    # Initialize the backend with this model
    backend = PBackend(noise_model=default_noise)
    # [backend_noise]
