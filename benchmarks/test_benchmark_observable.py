import pytest
import numpy as np
import copy
from pyrauli import (
    Observable,
    PauliTerm,
    PauliGate,
    CliffordGate,
    UnitalNoise,
    CoefficientTruncator,
    LambdaTruncator,
)

# --- Fixtures for Observable Benchmarks ---

@pytest.fixture(scope="module")
def large_observable_and_ops():
    """Provides a large observable and pre-generated random operations."""
    num_qubits = 1024
    num_ops = 1024
    np.random.seed(42)
    
    obs = Observable("".join(np.random.choice(["I", "X", "Y", "Z"], num_qubits)))
    
    # Pre-generate targets and gates to not benchmark this part
    pauli_gates = np.random.choice([PauliGate.X, PauliGate.Y, PauliGate.Z], num_ops)
    pauli_targets = np.random.randint(0, num_qubits, num_ops)
    
    clifford_gates = np.random.choice([CliffordGate.H], num_ops)
    clifford_targets = np.random.randint(0, num_qubits, num_ops)

    cx_targets = [
        tuple(np.random.choice(range(num_qubits), 2, replace=False))
        for _ in range(num_ops)
    ]
    
    unital_noises = np.random.choice([UnitalNoise.Depolarizing, UnitalNoise.Dephasing], num_ops)
    unital_targets = np.random.randint(0, num_qubits, num_ops)

    return {
        "obs": obs,
        "pauli_gates": pauli_gates,
        "pauli_targets": pauli_targets,
        "clifford_gates": clifford_gates,
        "clifford_targets": clifford_targets,
        "cx_targets": cx_targets,
        "unital_noises": unital_noises,
        "unital_targets": unital_targets
    }

@pytest.fixture(scope="module")
def observable_for_merge_and_truncate():
    """Provides an observable that has undergone a series of operations."""
    np.random.seed(42)
    obs = Observable("Z" * 8)
    
    for _ in range(32):
        gate_type = np.random.choice(["pauli", "clifford", "rz", "cx"])
        if gate_type == "pauli":
            obs.apply_pauli(np.random.choice([PauliGate.X, PauliGate.Y, PauliGate.Z]), np.random.randint(0, 8))
        elif gate_type == "clifford":
            obs.apply_clifford(CliffordGate.H, np.random.randint(0, 8))
        elif gate_type == "rz":
            obs.apply_rz(np.random.randint(0, 8), np.random.rand() * 2 * np.pi)
        elif gate_type == "cx":
            control, target = np.random.choice(range(8), 2, replace=False)
            obs.apply_cx(control, target)
    return obs
    
# --- Observable Primitive Benchmarks ---

def test_1024observable_apply_1024pauli(large_observable_and_ops, benchmark):
    obs = large_observable_and_ops["obs"]
    gates = large_observable_and_ops["pauli_gates"]
    targets = large_observable_and_ops["pauli_targets"]

    def apply_all_pauli():
        for gate, target in zip(gates, targets):
            obs.apply_pauli(gate, target)

    benchmark(apply_all_pauli)

def test_1024observable_apply_1024clifford(large_observable_and_ops, benchmark):
    obs = large_observable_and_ops["obs"]
    gates = large_observable_and_ops["clifford_gates"]
    targets = large_observable_and_ops["clifford_targets"]

    def apply_all_clifford():
        for gate, target in zip(gates, targets):
            obs.apply_clifford(gate, target)

    benchmark(apply_all_clifford)

def test_1024observable_apply_1024cx(large_observable_and_ops, benchmark):
    obs = large_observable_and_ops["obs"]
    targets = large_observable_and_ops["cx_targets"]
    
    def apply_all_cx():
        for control, target in targets:
            obs.apply_cx(control, target)
            
    benchmark(apply_all_cx)
    
def test_1024observable_apply_1024unital_noise(large_observable_and_ops, benchmark):
    obs = large_observable_and_ops["obs"]
    noises = large_observable_and_ops["unital_noises"]
    targets = large_observable_and_ops["unital_targets"]
    
    def apply_all_unital_noise():
        for noise, target in zip(noises, targets):
            obs.apply_unital_noise(noise, target, 0.01)

    benchmark(apply_all_unital_noise)

def test_1024observable_apply_8rz(benchmark):
    np.random.seed(42)
    thetas = np.random.rand(8) * 2 * np.pi
    targets = np.random.choice(range(32), 8, replace=False)

    def apply_all_rz():
        obs = Observable("X" * 32)
        for i in range(8):
            obs.apply_rz(targets[i], thetas[i])

    benchmark(apply_all_rz)

def test_1024observable_apply_8amplitude_damping(benchmark):
    np.random.seed(42)
    targets = np.random.choice(range(32), 8, replace=False)

    def apply_all_rz():
        obs = Observable("X" * 32)
        for i in range(8):
            obs.apply_amplitude_damping(targets[i], 0.01)

    benchmark(apply_all_rz)

def test_observable_merge(observable_for_merge_and_truncate, benchmark):
    obs = observable_for_merge_and_truncate
    benchmark(obs.merge)

def test_observable_truncate_coefficient(observable_for_merge_and_truncate, benchmark):
    obs = observable_for_merge_and_truncate
    obs.merge()
    truncator = CoefficientTruncator(0.1)
    benchmark(obs.truncate, truncator)

def test_observable_truncate_lambda(observable_for_merge_and_truncate, benchmark):
    obs = observable_for_merge_and_truncate
    obs.merge()
    # Similar to CoefficientTruncator, we want to measure overhead
    lambda_truncator = LambdaTruncator(lambda pt: pt.coefficient < 0.05)
    benchmark(obs.truncate, lambda_truncator)
