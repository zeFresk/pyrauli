import pytest
import numpy as np

# Conditional import for Qiskit
qiskit = pytest.importorskip("qiskit", minversion="1.0")

from qiskit.circuit import QuantumCircuit, ParameterVector
from qiskit.circuit.library import ZZFeatureMap, RealAmplitudes
from qiskit.circuit.random import random_circuit
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler import generate_preset_pass_manager

from pyrauli import from_qiskit, PBackend, PyrauliEstimator, NoiseModel, UnitalNoise, QGate, CoefficientTruncator

# --- Fixtures for Qiskit Benchmarks ---

@pytest.fixture(scope="module")
def qiskit_resources():
    """Provides pre-built Qiskit circuits and observables."""
    np.random.seed(42)
    
    # For observable conversion
    obs_list = [("".join(p), np.random.rand()) for p in np.random.choice(["I", "X", "Y", "Z"], (128, 128))]
    qiskit_obs = SparsePauliOp.from_list(obs_list)

    # For circuit conversion
    qiskit_circ_convert = QuantumCircuit(32)
    for i in range(32):
        gate = np.random.choice(["H", "CX", "Rz"])
        if gate == "H":
            qiskit_circ_convert.add_operation("H", qubit=(i % 32))
        elif gate == "CX":
            qiskit_circ_convert.add_operation("CX", control=(i % 32), target=((i + 1) % 32))
        elif gate == "Rz": # Rz
            qiskit_circ_convert.add_operation("Rz", qubit=(i % 32), param=np.random.rand())
        else:
            qiskit_circ_convert.add_operation(np.random.choice(["I", "X", "Y", "Z"]), qubit=(i % 32))

    return {
        "qiskit_obs": qiskit_obs,
        "qiskit_circ_convert": qiskit_circ_convert,
    }

# --- Qiskit Integration Benchmarks ---

def benchmark_qiskit_observable_conversion(benchmark, qiskit_resources):
    q_obs = qiskit_resources["qiskit_obs"]
    benchmark(from_qiskit, q_obs)

def benchmark_qiskit_circuit_conversion(benchmark, qiskit_resources):
    q_circ = qiskit_resources["qiskit_circ_convert"]
    benchmark(from_qiskit, q_circ)

def benchmark_qiskit_pbackend_run(benchmark):
    np.random.seed(42)
    backend = PBackend(num_qubits=16)
    pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
    qiskit_circ_run_raw = random_circuit(16, 16, seed=42, max_operands=2)
    qiskit_circ_run_transpiled = pm.run(qiskit_circ_run_raw)
    run_obs = SparsePauliOp("Z" * 16)
    def run_job():
        job = backend.run([(qiskit_circ_run_transpiled, run_obs)])
        job.result()
        
    benchmark(run_job)

def benchmark_qiskit_pbackend_parameterized_run(benchmark):
    np.random.seed(42)
    num_qubits_param = 16
    feature_map = ZZFeatureMap(feature_dimension=num_qubits_param, reps=1)
    ansatz = RealAmplitudes(num_qubits=num_qubits_param, reps=1)
    param_qc = feature_map.compose(ansatz)
    param_obs = SparsePauliOp("Z" * num_qubits_param)
    param_vals = np.random.rand(param_qc.num_parameters)

    # Setup estimator with noise and truncation
    noise_model = NoiseModel()
    noise_model.add_unital_noise_on_all_gates(UnitalNoise.Depolarizing, 0.01)
    
    estimator = PyrauliEstimator(
        noise_model=noise_model,
    )
    
    def run_job():
        job = estimator.run([(param_qc, param_obs, param_vals)])
        job.result()
        
    benchmark(run_job)
