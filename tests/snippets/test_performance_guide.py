import pyrauli
import pytest

def test_single_parallel_snippet():
    # [single_parallel]
    circuit = pyrauli.Circuit(4)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.cx(1, 2)
    circuit.rz(2, 0.5)
    circuit.cx(2, 3)

    observable = pyrauli.Observable("ZIII")

    # Run the simulation for one observable using the parallel policy
    ev, err = circuit.expectation_value(observable, runtime=pyrauli.par)

    print(f"Expectation value (parallel): {ev}")
    # [single_parallel]
    assert isinstance(ev, float)

def test_batch_observables_snippet():
    # [batch_observables]
    circuit = pyrauli.Circuit(4)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.cx(1, 2)
    circuit.rz(2, 0.5)
    circuit.cx(2, 3)

    observables = [
        pyrauli.Observable("ZIII"),
        pyrauli.Observable("IZII"),
        pyrauli.Observable("IIZI"),
        pyrauli.Observable("IIIZ"),
    ]

    # Run the simulation for the batch of observables in parallel
    results = circuit.expectation_value(observables, runtime=pyrauli.par)

    for i, (ev, err) in enumerate(results):
        print(f"Observable {i}: EV = {ev:.4f}, Error = {err:.4f}")
    # [batch_observables]
    assert len(results) == 4

# Skip this entire module if qiskit is not installed
qiskit = pytest.importorskip("qiskit", reason="Qiskit extra not installed")

from qiskit.circuit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp

def test_qiskit_parallel_snippet():
    # [qiskit_parallel]
    from pyrauli import PBackend

    # Initialize the backend with the parallel execution policy as the default
    backend = PBackend(runtime=pyrauli.par)

    # All jobs run on this backend will now use the parallel engine by default
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    observables = [SparsePauliOp("ZI"), SparsePauliOp("IZ")]

    job = backend.run([(qc, observables)])
    result = job.result()
    
    print(f"Expectation values: {result[0].data.evs}")
    # [qiskit_parallel]
    assert len(result[0].data.evs) == 2
