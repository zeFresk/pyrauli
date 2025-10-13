import pytest
import math
from pyrauli import (
    Observable,
    PauliTerm,
    Circuit,
    CoefficientTruncator,
    WeightTruncator,
    KeepNTruncator,
    LambdaTruncator,
    MultiTruncator,
    AlwaysAfterSplittingPolicy,
    NeverTruncator
)

# --- Direct Observable.truncate() Tests ---

def test_coefficient_truncator_on_observable():
    """Tests that terms with small coefficients are removed."""
    # [truncator_coeff]
    obs = Observable([PauliTerm("I", 0.99), PauliTerm("Y", 0.01)])
    truncator = CoefficientTruncator(0.1)
    
    removed_count = obs.truncate(truncator) # 1
    # [truncator_coeff]
    assert removed_count == 1
    assert len(obs) == 1
    assert obs[0] == PauliTerm("I", 0.99)

def test_weight_truncator_on_observable():
    """Tests that terms with high Pauli weight are removed."""
    obs = Observable([PauliTerm("IIII", 0.5), PauliTerm("YYYY", 0.5)])
    # Keep terms with weight < 4
    truncator = WeightTruncator(4)
    
    removed_count = obs.truncate(truncator)
    
    assert removed_count == 1
    assert len(obs) == 1
    assert obs[0] == PauliTerm("IIII", 0.5)

def test_keepn_truncator_on_observable():
    """Tests that terms with high Pauli weight are removed."""
    obs = Observable([PauliTerm("IIII", 0.5), PauliTerm("ZYXI", 0.11), PauliTerm("YYYY", -0.6), PauliTerm("IXYZ", 0.1), PauliTerm("IIIX", -0.4)])

    truncator = KeepNTruncator(2)
    
    removed_count = obs.truncate(truncator)
    
    assert removed_count == 3
    assert len(obs) == 2
    assert (obs[0] == PauliTerm("IIII", 0.5)) or (obs[0] == PauliTerm("YYYY", -0.6))
    assert (obs[1] == PauliTerm("IIII", 0.5)) or (obs[1] == PauliTerm("YYYY", -0.6))

def test_lambda_truncator_on_observable_def():
    """Tests truncation based on a custom Python function."""
    # This predicate removes any term containing a 'Y'
    def remove_if_has_y(pauli_term: PauliTerm):
        # not optimized!
        return 'Y' in repr(pauli_term)

    obs = Observable([PauliTerm("IXI", 0.5), PauliTerm("IZY", 0.5)])
    truncator = LambdaTruncator(remove_if_has_y)
    
    removed_count = obs.truncate(truncator)
    
    assert removed_count == 1
    assert len(obs) == 1
    assert obs[0] == PauliTerm("IXI", 0.5)


def test_lambda_truncator_on_observable_lbd():
    """Tests truncation based on a custom Python function."""
    # [truncator_lambda]
    obs = Observable([PauliTerm("IXI", 0.5), PauliTerm("IZY", 0.5)])
    truncator = LambdaTruncator(lambda pt: 'Y' in repr(pt))
    
    removed_count = obs.truncate(truncator) # 1 (removed IZY)
    # [truncator_lambda]
    
    assert removed_count == 1
    assert len(obs) == 1
    assert obs[0] == PauliTerm("IXI", 0.5)

def test_multi_truncators_fully_dynamic():
    """Tests truncation using MultiTruncator on two Python truncators."""
    obs = Observable([PauliTerm("IXI", 0.5), PauliTerm("IYI", 0.5), PauliTerm("IZI", 0.5)])
    
    def truncator_X_fn(pt: PauliTerm):
        return 'X' in repr(pt)
    truncator_Y = LambdaTruncator(lambda pt: 'Y' in repr(pt))
    multi_truncator = MultiTruncator([LambdaTruncator(truncator_X_fn), truncator_Y])
    
    removed_count = obs.truncate(multi_truncator)
    
    assert removed_count == 2
    assert len(obs) == 1
    assert obs[0] == PauliTerm("IZI", 0.5)

# --- Circuit Truncation Tests ---

def test_truncator_in_circuit():
    """
    Tests that a truncator is correctly applied by the circuit's scheduler.
    """
    # [truncator_coefficient]
    qc = Circuit(
        nb_qubits=4,
        truncator=CoefficientTruncator(0.1),
        # Crucially, the policy must be set to run the truncator
        truncate_policy=AlwaysAfterSplittingPolicy()
    )
    # [truncator_coefficient]

    # This sequence of gates creates a large number of terms
    for i in range(4):
        qc.add_operation("H", qubit=i)
        qc.add_operation("Rz", qubit=i, param=0.2) # Small angle -> small coeffs
        qc.add_operation("H", qubit=i)

    # Run the circuit
    obs_in = Observable("ZZZZ")
    obs_out = qc.run(obs_in)

    # Create a reference circuit without truncation
    qc_ref = Circuit(4)
    for i in range(4):
        qc_ref.add_operation("H", qubit=i)
        qc_ref.add_operation("Rz", qubit=i, param=0.2)
        qc_ref.add_operation("H", qubit=i)
    
    obs_out_ref = qc_ref.run(obs_in)

    # Assert that the truncation was effective
    assert len(obs_out) < len(obs_out_ref)
    
    # Check that all remaining terms have a coefficient >= 0.1
    for term in obs_out:
        assert abs(term.coefficient) >= 0.1

def test_circuit_set_truncator():
    """Tests that the truncator can be updated after circuit creation."""
    qc = Circuit(4) # Initially has NeverTruncator
    
    # This circuit will generate 2^4 = 16 terms
    for i in range(4):
        qc.add_operation("AMPLITUDEDAMPING", i, 0.5)
    
    # Run without an effective truncator (default is NeverTruncator)
    obs_in = Observable("ZZZZ")
    obs_out_no_trunc = qc.run(obs_in)
    assert len(obs_out_no_trunc) == 16

    # Now, set an effective truncator and policy
    qc.set_truncator(CoefficientTruncator(0.3))
    qc.set_truncate_policy(AlwaysAfterSplittingPolicy())
    
    # Re-run the same simulation
    obs_out_with_trunc = qc.run(obs_in)
    
    # Assert that truncation has occurred
    assert len(obs_out_with_trunc) < 16

def test_multi_truncator_in_circuit():
    """Tests that a combined truncator works correctly within a Circuit."""
    # Create individual truncators
    weight_trunc = WeightTruncator(3) # Keep only weight 1 and 2 terms
    coeff_trunc = CoefficientTruncator(0.2) # Keep only terms with |coeff| >= 0.2

    # Combine them
    combined_truncator = MultiTruncator([weight_trunc, coeff_trunc])
    
    qc = Circuit(
        nb_qubits=5,
        truncator=combined_truncator,
        truncate_policy=AlwaysAfterSplittingPolicy()
    )

    # This circuit creates a mix of terms with different weights and coefficients
    for i in range(4):
        qc.add_operation("H", qubit=i)
        qc.add_operation("Rz", qubit=i, param=0.4) # Angle chosen to produce varied coeffs

    obs_in = Observable("IIZII")
    obs_out = qc.run(obs_in)

    # Verify that all remaining terms satisfy BOTH conditions
    assert len(list(obs_out)) > 0 # Ensure we didn't truncate everything
    for term in obs_out:
        assert term.pauli_weight() < 3
        assert abs(term.coefficient) >= 0.2

def test_truncator_error_tracking():
    # [truncator_error]
    # Use a truncator that will remove terms with small coefficients
    truncator = CoefficientTruncator(0.1)
    
    circuit = Circuit(2, truncator=truncator)
    circuit.h(0)
    circuit.h(1)
    circuit.cx(0, 1)
    circuit.rz(1, 0.01) # This gate splits the observable
    circuit.h(0)
    circuit.h(1)

    observable = Observable("ZZ")

    # The second value returned is the estimated error
    ev, err = circuit.expectation_value(observable)
    print(circuit.run(observable))

    print(f"Expectation value: {ev:.4f}")
    print(f"Estimated truncation error: {err:.4f}")
    
    # For comparison, run without truncation 
    circuit.set_truncator(NeverTruncator())

    exact_ev, _ = circuit.expectation_value(observable)
    print(f"Exact expectation value: {exact_ev:.4f}")
    print(f"Actual error: {abs(exact_ev - ev):.4f}")
    # [truncator_error]
    assert err > 0
    assert abs(exact_ev - ev) <= 0.1 # Check that error tracking is accurate
