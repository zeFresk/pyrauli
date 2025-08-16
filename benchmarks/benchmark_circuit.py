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
    AlwaysAfterSplittingPolicy
)

# --- Fixtures for Circuit Benchmarks ---

@pytest.fixture(scope="module")
def circuit_for_run_benchmark():
    """Creates a circuit and observable for run-based benchmarks."""
    np.random.seed(42)
    qc = Circuit(8)
    obs_in = Observable("Z" * 8)

    # Add a sequence of gates that will cause splitting
    for i in range(8):
        qc.add_operation("H", i)
    for _ in range(8):
        qc.add_operation("Rz", qubit=np.random.randint(0, 8), param=np.random.rand())

    for _ in range(24):
        gate_type = np.random.choice(["H", "CX"])
        if gate_type == "H":
            qc.add_operation("H", qubit=np.random.randint(0, 8))
        else:
            c, t = np.random.choice(range(8), 2, replace=False)
            qc.add_operation("CX", control=c, target=t)
            
    return qc, obs_in

@pytest.fixture(scope="module")
def noisy_circuit_for_run_benchmark():
    """Creates a circuit and observable for run-based benchmarks."""
    np.random.seed(42)

    # Setup noise model
    noise_model = NoiseModel()
    noise_model.add_amplitude_damping_on_gate(QGate.CX, 0.02)
    noise_model.add_unital_noise_on_gate(QGate.CX, UnitalNoise.AmplitudeDamping, 0.01)

    noise_model.add_unital_noise_on_gate(QGate.X, UnitalNoise.Depolarizing, 0.01)
    noise_model.add_unital_noise_on_gate(QGate.Y, UnitalNoise.Depolarizing, 0.01)
    noise_model.add_unital_noise_on_gate(QGate.Z, UnitalNoise.Depolarizing, 0.01)

    noise_model.add_unital_noise_on_gate(QGate.H, UnitalNoise.Depolarizing, 0.01)
    noise_model.add_amplitude_damping_on_gate(QGate.H, 0.01)

    noise_model.add_amplitude_damping_on_gate(QGate.Rz, 0.01)
    noise_model.add_unital_noise_on_gate(QGate.Rz, UnitalNoise.Dephasing, 0.01)

    qc = Circuit(8, noise_model=noise_model)

    obs_in = Observable("Z" * 8)

    # Add a sequence of gates that will cause splitting
    for i in range(8):
        qc.add_operation("H", i)
    for _ in range(8):
        qc.add_operation("Rz", qubit=np.random.randint(0, 8), param=np.random.rand())

    for _ in range(24):
        gate_type = np.random.choice(["H", "CX"])
        if gate_type == "H":
            qc.add_operation("H", qubit=np.random.randint(0, 8))
        else:
            c, t = np.random.choice(range(8), 2, replace=False)
            qc.add_operation("CX", control=c, target=t)
            
    return qc, obs_in

# --- Circuit Benchmarks ---

def benchmark_circuit_construction(benchmark):
    """Times the construction of a large circuit, without running it."""
    num_qubits = 1024
    num_gates = 1024
    np.random.seed(42)

    def build_circuit():
        qc = Circuit(num_qubits)
        for i in range(num_gates):
            gate = np.random.choice(["H", "CX", "Rz"])
            if gate == "H":
                qc.add_operation("H", qubit=(i % num_qubits))
            elif gate == "CX":
                qc.add_operation("CX", control=(i % num_qubits), target=((i + 1) % num_qubits))
            else: # Rz
                qc.add_operation("Rz", qubit=(i % num_qubits), param=np.random.rand())
    
    benchmark(build_circuit)

def benchmark_circuit_run_with_truncator(benchmark, circuit_for_run_benchmark):
    """Times a circuit run with a combined truncator and merge policy."""
    qc, obs_in = circuit_for_run_benchmark
    
    # Setup truncator and policies
    combined_truncator = MultiTruncator([
        CoefficientTruncator(0.01),
        WeightTruncator(4)
    ])
    qc.set_truncator(combined_truncator)
    qc.set_truncate_policy(AlwaysAfterSplittingPolicy())
    qc.set_merge_policy(AlwaysAfterSplittingPolicy()) # Using the same for simplicity

    # The benchmark excludes the setup time above
    benchmark(qc.run, obs_in)

def benchmark_circuit_run_with_noise_model_and_truncators(benchmark, noisy_circuit_for_run_benchmark):
    """Times a circuit run with a complex noise model."""
    qc, obs_in = noisy_circuit_for_run_benchmark

    # Setup noise model
    noise_model = NoiseModel()
    noise_model.add_amplitude_damping_on_gate(QGate.CX, 0.02)
    noise_model.add_unital_noise_on_gate(QGate.CX, UnitalNoise.AmplitudeDamping, 0.01)
    noise_model.add_unital_noise_on_gate(QGate.X, UnitalNoise.Depolarizing, 0.01)
    noise_model.add_unital_noise_on_gate(QGate.Y, UnitalNoise.Depolarizing, 0.01)
    noise_model.add_unital_noise_on_gate(QGate.Z, UnitalNoise.Depolarizing, 0.01)
    noise_model.add_amplitude_damping_on_gate(QGate.Rz, 0.01)
    noise_model.add_unital_noise_on_gate(QGate.Rz, UnitalNoise.Dephasing, 0.01)

    qc.set_truncator(CoefficientTruncator(0.01))
    qc.set_truncate_policy(AlwaysAfterSplittingPolicy())
    qc.set_merge_policy(AlwaysAfterSplittingPolicy()) # Using the same for simplicity


    # Benchmark the run of the noisy circuit
    benchmark(qc.run, obs_in)
