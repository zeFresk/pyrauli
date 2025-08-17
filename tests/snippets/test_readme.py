import pytest 
import pyrauli

def test_readme_quick_start():
    # 1. Initialize a 2-qubit circuit
    circuit = pyrauli.Circuit(2)

    # 2. Add quantum operations
    circuit.add_operation("H", 0)      # Hadamard on qubit 0
    circuit.add_operation("CX", 0, 1)  # CNOT with control 0, target 1

    # 3. Define an observable
    # Here, we measure the Pauli Z observable on qubit 0
    observable = pyrauli.Observable("ZI")

    # 4. Run the simulation
    # This evolves the observable backward through the circuit
    final_observable = circuit.run(observable)

    # 5. Retrieve the final expectation value
    # The expectation value is calculated with respect to the initial |00...0> state
    expectation_value = final_observable.expectation_value()

    print(f"Final observable: {final_observable}")
    print(f"Expectation value <Z_0>: {expectation_value}")

    assert final_observable == pyrauli.Observable("XI", 1.0)
    assert expectation_value == pytest.approx(0)


qiskit = pytest.importorskip("qiskit", reason="Qiskit extra not installed")
from qiskit.circuit import QuantumCircuit, Parameter
from qiskit.transpiler import generate_preset_pass_manager
from qiskit.quantum_info import SparsePauliOp
from pyrauli import PBackend

def test_readme_qiskit():
    # Create a parameterized Qiskit circuit
    theta = Parameter('theta')
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.rz(theta, 0)
    qc.cx(0, 1)

    # Define an observable and instantiate the backend
    obs = SparsePauliOp("ZI")
    backend = PBackend()

    # transpilation is supported (but not needed here)
    pm = generate_preset_pass_manager(backend)
    isa_qc = pm.run(qc)

    # Run using the PUB (Primitive Unified Bloc) format
    job = backend.run([(qc, obs, [3.14])])
    result = job.result()
    ev = result[0].data.evs[0]

    print(f"Expectation value: {ev}")
    assert ev == pytest.approx(0.0)
