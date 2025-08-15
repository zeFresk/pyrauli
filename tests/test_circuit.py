import pytest
import math

from pyrauli import (
    Circuit,
    Observable,
    CoefficientTruncator,
    NoiseModel,
    NeverPolicy,
    AlwaysBeforeSplittingPolicy,
    AlwaysAfterSplittingPolicy,
    NeverTruncator,
)

# --- Test Circuit Initialization ---


def test_init():
    """Tests basic circuit initialization."""
    qc = Circuit(4)
    assert qc.nb_qubits() == 4


def test_init_with_policies_and_truncator():
    """Tests circuit initialization with custom policies and truncator."""
    truncator = CoefficientTruncator(0.001)
    noise_model = NoiseModel()
    merge_policy = NeverPolicy()
    truncate_policy = AlwaysBeforeSplittingPolicy()

    qc = Circuit(
        nb_qubits=4,
        truncator=truncator,
        noise_model=noise_model,
        merge_policy=merge_policy,
        truncate_policy=truncate_policy,
    )
    assert qc.nb_qubits() == 4


# --- Test Gate Application ---


def test_add_operations():
    """Tests adding various gate types does not raise errors."""
    qc = Circuit(2)
    # Pauli Gates
    qc.add_operation("I", qubit=0)
    qc.add_operation("X", qubit=0)
    qc.add_operation("Y", qubit=0)
    qc.add_operation("Z", qubit=0)
    # Clifford Gate
    qc.add_operation("H", qubit=0)
    # Rotation Gate
    qc.add_operation("Rz", qubit=0, param=math.pi)
    # Control Gate
    qc.add_operation("CX", control=0, target=1)


def test_add_noise_channels():
    """Tests adding noise channels does not raise errors."""
    qc = Circuit(2)
    qc.add_operation("AMPLITUDEDAMPING", qubit=0, param=0.01)
    qc.add_operation("DEPOLARIZING", qubit=0, param=0.01)
    qc.add_operation("DEPHASING", qubit=0, param=0.01)


def test_add_operation_is_case_insensitive():
    """Tests that gate names are not case-sensitive."""
    qc = Circuit(2)
    qc.add_operation("h", qubit=0)
    qc.add_operation("rz", qubit=0, param=math.pi)
    qc.add_operation("Cx", control=0, target=1)


# --- Test Error Handling ---


def test_add_bad_gate_raises_error():
    """Tests that adding an unsupported gate string raises an error."""
    qc = Circuit(2)
    with pytest.raises(IndexError):
        qc.add_operation("invalid_gate", qubit=0)
    with pytest.raises(IndexError):
        qc.add_operation("XX", qubit=0)


def test_add_operation_with_bad_qubit_indices_raises_error():
    """Tests that out-of-bounds or invalid qubit indices raise errors."""
    qc = Circuit(4)
    with pytest.raises(ValueError):
        qc.add_operation("H", qubit=4)
    with pytest.raises(ValueError):
        qc.add_operation("CX", control=0, target=4)
    with pytest.raises(ValueError):
        qc.add_operation("CX", control=4, target=0)
    with pytest.raises(ValueError):
        qc.add_operation("CX", control=1, target=1)


def test_run_with_mismatched_observable_raises_error():
    """Tests that running with an observable of the wrong size raises an error."""
    qc = Circuit(4)
    bad_obs_small = Observable("II")
    bad_obs_big = Observable("IIZZZ")
    with pytest.raises(ValueError):
        qc.run(bad_obs_small)
    with pytest.raises(ValueError):
        qc.run(bad_obs_big)


# --- Test Simulation Logic ---


def test_simple_run():
    """Tests a simple identity circuit."""
    qc = Circuit(1)
    qc.add_operation("I", qubit=0)
    obs = Observable("I")
    result_obs = qc.run(obs)
    assert result_obs.expectation_value() == pytest.approx(1.0)


def test_merge_with_scheduler():
    """Tests that the merge policy is correctly applied."""
    qc = Circuit(
        nb_qubits=1,
        truncator=NeverTruncator(),
        noise_model=NoiseModel(),
        merge_policy=AlwaysAfterSplittingPolicy(),
        truncate_policy=NeverPolicy(),
    )
    qc.add_operation("rz", qubit=0, param=1.0)
    qc.add_operation("rz", qubit=0, param=-1.0)
    result_obs = qc.run(Observable(["X", "X"]))
    assert result_obs.size() == 2

def p1_to_ev(p1):
        return 1.0 - (2.0 * p1)

def test_qasm_benchmark_circuit():
    """Translates a more complex circuit from the C++ tests and verifies results."""
    qc = Circuit(4)

    for i in range(4):
        qc.add_operation("H", i)

    qc.add_operation("Rz", 0, -math.pi / 2.0)
    qc.add_operation("Rz", 1, -math.pi / 3.0)
    qc.add_operation("Rz", 2, -math.pi / 4.0)
    qc.add_operation("Rz", 3, -math.pi / 5.0)

    qc.add_operation("cx", 0, 1)
    qc.add_operation("cx", 2, 3)
    qc.add_operation("cx", 1, 2)

    for i in range(4):
        qc.add_operation("H", i)

    test_cases = {
        "ZIII": p1_to_ev(0.500000),
        "IZII": p1_to_ev(0.356999),
        "IIZI": p1_to_ev(0.213950),
        "IIIZ": p1_to_ev(0.095499),
    }

    for obs_str, expected_ev in test_cases.items():
        res = qc.run(Observable(obs_str))
        assert res.expectation_value() == pytest.approx(expected_ev, abs=1e-4)


qiskit = pytest.importorskip("qiskit", reason="Qiskit extra not installed")
from qiskit.circuit import QuantumCircuit, Parameter

# Import the pyrauli components needed for the test
from pyrauli import from_qiskit


def test_from_qiskit_bell_state():
    """
    Tests the from_qiskit converter by comparing its output to a manually
    constructed pyrauli circuit.
    """
    # 1. Define a simple Qiskit circuit (Bell state)
    qc_qiskit = QuantumCircuit(2)
    qc_qiskit.h(0)
    qc_qiskit.cx(0, 1)

    # 2. Manually create the equivalent pyrauli circuit
    qc_manual = Circuit(2)
    qc_manual.add_operation("H", qubit=0)
    qc_manual.add_operation("CX", control=0, target=1)

    # 3. Use the converter to create a pyrauli circuit from the Qiskit one
    qc_converted = from_qiskit(qc_qiskit)

    # 4. Define an observable to test against
    observable = Observable("ZI")

    # 5. Run the simulation on both pyrauli circuits
    result_manual = qc_manual.run(observable)
    result_converted = qc_converted.run(observable)

    # 6. Assert that the results are identical
    # For a Bell state, the expectation value of ZI is 0.
    expected_ev = 0.0

    assert result_manual.expectation_value() == pytest.approx(expected_ev)
    assert result_converted.expectation_value() == pytest.approx(expected_ev)
    assert result_manual == result_converted


def test_from_qiskit_parameterized_circuit():
    """
    Tests the converter with a parameterized Qiskit circuit.
    """
    theta = Parameter("θ")

    qc_qiskit = QuantumCircuit(1)
    qc_qiskit.h(0)
    qc_qiskit.rz(theta, 0)
    qc_qiskit.h(0)

    # Bind the parameter to a specific value
    bound_qc = qc_qiskit.assign_parameters({theta: math.pi / 3})

    # 2. Manually create the equivalent pyrauli circuit
    qc_manual = Circuit(1)
    qc_manual.add_operation("H", qubit=0)
    qc_manual.add_operation("Rz", qubit=0, param=math.pi / 3)
    qc_manual.add_operation("H", qubit=0)

    # 3. Convert the bound Qiskit circuit
    qc_converted = from_qiskit(bound_qc)

    # 4. Run with an observable and assert equality
    observable = Observable("Z")
    result_manual = qc_manual.run(observable)
    result_converted = qc_converted.run(observable)

    expected_ev = p1_to_ev(0.25)

    assert result_manual.expectation_value() == pytest.approx(expected_ev)
    assert result_converted.expectation_value() == pytest.approx(expected_ev)
    assert result_converted == result_manual
