import pytest
import numpy as np
from pyrauli import (
    Circuit,
    Observable,
    NoiseModel,
    QGate,
    UnitalNoise,
    CoefficientTruncator,
    WeightTruncator,
    MultiTruncator,
    NeverTruncator,
    AlwaysAfterSplittingPolicy
)

# --- Fixtures for Circuit Benchmarks ---

@pytest.fixture(scope="module")
def circuit_for_run_benchmark():
    """Creates a circuit and observable for run-based benchmarks."""
    np.random.seed(42)
    qc = Circuit(16)
    obs_in = Observable("X" * 16)

    # Add a sequence of gates that will cause splitting
    for i in range(16):
        qc.add_operation("H", i)
    for _ in range(16):
        qc.add_operation("Rz", qubit=np.random.randint(0, 16), param=np.random.rand())

    for _ in range(24):
        gate_type = np.random.choice(["H", "CX"])
        if gate_type == "H":
            qc.add_operation("H", qubit=np.random.randint(0, 16))
        else:
            c, t = np.random.choice(range(16), 2, replace=False)
            qc.add_operation("CX", control=c, target=t)
            
    return qc, obs_in

@pytest.fixture(scope="module")
def noisy_circuit_for_run_benchmark():
    """Creates a circuit and observable for run-based benchmarks."""
    np.random.seed(42)

    # Setup noise model
    noise_model = NoiseModel()
    noise_model.add_amplitude_damping_on_gate(QGate.Cx, 0.02)
    noise_model.add_unital_noise_on_gate(QGate.Cx, UnitalNoise.Depolarizing, 0.02)

    noise_model.add_unital_noise_on_gate(QGate.X, UnitalNoise.Depolarizing, 0.01)
    noise_model.add_unital_noise_on_gate(QGate.Y, UnitalNoise.Depolarizing, 0.01)
    noise_model.add_unital_noise_on_gate(QGate.Z, UnitalNoise.Depolarizing, 0.01)

    noise_model.add_unital_noise_on_gate(QGate.H, UnitalNoise.Depolarizing, 0.01)
    noise_model.add_amplitude_damping_on_gate(QGate.H, 0.01)

    noise_model.add_amplitude_damping_on_gate(QGate.Rz, 0.01)
    noise_model.add_unital_noise_on_gate(QGate.Rz, UnitalNoise.Dephasing, 0.01)

    qc = Circuit(16, noise_model=noise_model)

    obs_in = Observable("Z" * 16)

    # Add a sequence of gates that will cause splitting
    for i in range(16):
        qc.add_operation("H", i)
    for _ in range(16):
        qc.add_operation("Rz", qubit=np.random.randint(0, 16), param=np.random.rand())

    for _ in range(24):
        gate_type = np.random.choice(["H", "CX"])
        if gate_type == "H":
            qc.add_operation("H", qubit=np.random.randint(0, 16))
        else:
            c, t = np.random.choice(range(16), 2, replace=False)
            qc.add_operation("CX", control=c, target=t)
            
    return qc, obs_in

# --- Circuit Benchmarks ---

def test_circuit1024x1024_construction(benchmark):
    """Times the construction of a large circuit, without running it."""
    num_qubits = 1024
    num_gates = 1024
    np.random.seed(42)

    def build_circuit():
        qc = Circuit(num_qubits)
        for i in range(num_gates):
            gate = np.random.choice(["H", "CX", "Rz", "P"])
            if gate == "H":
                qc.add_operation("H", qubit=(i % num_qubits))
            elif gate == "CX":
                qc.add_operation("CX", control=(i % num_qubits), target=((i + 1) % num_qubits))
            elif gate == "Rz": # Rz
                qc.add_operation("Rz", qubit=(i % num_qubits), param=np.random.rand())
            else:
                qc.add_operation(np.random.choice(["I", "X", "Y", "Z"]), qubit=(i % num_qubits))
    
    benchmark(build_circuit)

def test_circuit1024x1024clifford_run(benchmark):
    np.random.seed(42)
    qc = Circuit(1024)
    for _ in range(1024):
        gate_type = np.random.choice(["pauli", "clifford", "cx"])
        if gate_type == "pauli":
            qc.add_operation(np.random.choice(["I", "X", "Y", "Z"]), np.random.randint(0, 1024))
        elif gate_type == "clifford":
            qc.add_operation("H", np.random.randint(0, 1024))
        elif gate_type == "cx":
            control, target = np.random.choice(range(1024), 2, replace=False)
            qc.add_operation("cx", control=control, target=target)
    
    obs = Observable("".join(np.random.choice(["I", "X", "Y", "Z"], 1024)))

    benchmark(qc.run, obs)

def test_circuit16x32_run_without_truncator(circuit_for_run_benchmark, benchmark):
    """Times a circuit run with a combined truncator and merge policy."""
    qc, obs_in = circuit_for_run_benchmark
    
    qc.set_truncator(NeverTruncator())
    qc.set_truncate_policy(AlwaysAfterSplittingPolicy())
    qc.set_merge_policy(AlwaysAfterSplittingPolicy()) # Using the same for simplicity

    # The benchmark excludes the setup time above
    benchmark(qc.run, obs_in)

def test_circuit16x32_run_with_truncator(circuit_for_run_benchmark, benchmark):
    """Times a circuit run with a combined truncator and merge policy."""
    qc, obs_in = circuit_for_run_benchmark
    
    # Setup truncator and policies
    qc.set_truncator(CoefficientTruncator(0.01))
    qc.set_truncate_policy(AlwaysAfterSplittingPolicy())
    qc.set_merge_policy(AlwaysAfterSplittingPolicy()) # Using the same for simplicity

    # The benchmark excludes the setup time above
    benchmark(qc.run, obs_in)

def test_circuit16x32_run_with_noise_model_and_truncators(noisy_circuit_for_run_benchmark, benchmark):
    """Times a circuit run with a complex noise model."""
    qc, obs_in = noisy_circuit_for_run_benchmark

    qc.set_truncator(CoefficientTruncator(0.01))
    qc.set_truncate_policy(AlwaysAfterSplittingPolicy())
    qc.set_merge_policy(AlwaysAfterSplittingPolicy()) # Using the same for simplicity


    # Benchmark the run of the noisy circuit
    benchmark(qc.run, obs_in)
