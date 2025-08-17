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

qiskit = pytest.importorskip("qiskit", reason="Qiskit extra not installed")
from qiskit.circuit import QuantumCircuit, Parameter

# Import the pyrauli components needed for the test
from pyrauli import from_qiskit

def p1_to_ev(p1):
        return 1.0 - (2.0 * p1)

def test_from_qiskit_bell_state():
    """
    Tests the from_qiskit converter by comparing its output to a manually
    constructed pyrauli circuit.
    """
    # [from_qiskit]
    # 1. Define a simple Qiskit circuit (Bell state)
    qc_qiskit = QuantumCircuit(2)
    qc_qiskit.h(0)
    qc_qiskit.cx(0, 1)
    
    # 2. Convert it to a pyrauli.Circuit
    qc_converted = from_qiskit(qc_qiskit)
    # [from_qiskit]

    # 2. Manually create the equivalent pyrauli circuit
    qc_manual = Circuit(2)
    qc_manual.add_operation("H", qubit=0)
    qc_manual.add_operation("CX", control=0, target=1)

    # 3. Use the converter to create a pyrauli circuit from the Qiskit one

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
