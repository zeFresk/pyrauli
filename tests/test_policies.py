import pytest
from pyrauli import (
    Circuit,
    Observable,
    LambdaPolicy,
    NeverTruncator,
    SimulationState,
    OperationType,
    Timing
)

def test_lambda_policy_in_circuit():
    """
    Tests a custom scheduling policy defined in Python.
    
    The policy will be to only merge terms *after* the 2nd splitting gate.
    """
    # [policy_lambda]
    # 1. Define the custom policy as a Python function
    def merge_after_second_split(state: SimulationState, op_type: OperationType, timing: Timing) -> bool:
        """This policy returns True only for a Merge event after 2 splitting gates have been applied."""
        
        # We only care about the 'After' timing for merges
        if timing != Timing.After:
            return False
            
        # We only care about SplittingGate operations
        if op_type != OperationType.SplittingGate:
            return False
            
        # The core logic: check the number of splitting gates already applied.
        if state.nb_splitting_gates_applied == 2:
            return True
            
        return False

    # 2. Create the LambdaPolicy from the Python function
    custom_merge_policy = LambdaPolicy(merge_after_second_split)

    # 3. Create a circuit that uses this policy
    qc = Circuit(
        nb_qubits=1,
        truncator=NeverTruncator(),
        merge_policy=custom_merge_policy
    )

    # 4. Build a circuit with two splitting gates (Rz)
    # Each Rz gate will double the number of terms in the observable.
    qc.add_operation("Rz", qubit=0, param=0.5)  # 1st splitting gate
    qc.add_operation("Rz", qubit=0, param=0.5)  # 2nd splitting gate
    
    # 5. Run the simulation
    # The 'X' observable will split into 2 terms at the first Rz, and then 4 terms at the second.
    # The merge policy should trigger *only* after the second Rz, merging the 4 terms back down.
    obs_in = Observable("X")
    obs_out = qc.run(obs_in)
    # [policy_lambda]

    # 6. Assert the outcome
    # Without merging, there would be 4 terms.
    # Because our policy merges after the second split, the terms should be combined.
    # For this specific sequence (Rz(0.5) then Rz(0.5)), the terms merge back to 2.
    assert len(obs_out) == 2
