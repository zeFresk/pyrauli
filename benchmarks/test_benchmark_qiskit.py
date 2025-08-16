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
    for i in range(32*32):
        gate = np.random.choice(["H", "CX", "Rz"])
        if gate == "H":
            qiskit_circ_convert.h(i % 32)
        elif gate == "CX":
            qiskit_circ_convert.cx(i % 32, np.random.choice([k for k in range(32) if k != (i%32)]))
        elif gate == "Rz": # Rz
            qiskit_circ_convert.rz(np.random.rand() * np.pi, i % 32)
        else:
            pg = np.random.choice(["I", "X", "Y", "Z"])
            qubit= i % 32
            if pg == "I":
                qiskit_circ_convert.i(qubit)
            elif pg == "X":
                qiskit_circ_convert.x(qubit)
            elif pg == "Y":
                qiskit_circ_convert.y(qubit)
            elif pg == "Z":
                qiskit_circ_convert.z(qubit)

    return {
        "qiskit_obs": qiskit_obs,
        "qiskit_circ_convert": qiskit_circ_convert,
    }

# --- Qiskit Integration Benchmarks ---

def test_qiskit_1024observable_conversion(qiskit_resources, benchmark):
    q_obs = qiskit_resources["qiskit_obs"]
    benchmark(from_qiskit, q_obs)

def test_qiskit_32x32circuit_conversion(qiskit_resources, benchmark):
    q_circ = qiskit_resources["qiskit_circ_convert"]
    benchmark(from_qiskit, q_circ)

def test_qiskit_pbackend_run8x8(benchmark):
    np.random.seed(42)
    backend = PBackend(num_qubits=8)
    pm = generate_preset_pass_manager(backend=backend, optimization_level=0)
    qiskit_circ_run_raw = random_circuit(8, 8, seed=42, max_operands=2)
    qiskit_circ_run_transpiled = pm.run(qiskit_circ_run_raw)
    run_obs = SparsePauliOp("Z" * 8)
    def run_job():
        job = backend.run([(qiskit_circ_run_transpiled, run_obs)])
        job.result()
        
    benchmark(run_job)

def test_qiskit_pbackend_parameterized_zz_real_amp8x8(benchmark):
    np.random.seed(42)
    num_qubits_param = 8
    feature_map = ZZFeatureMap(feature_dimension=num_qubits_param, reps=1)
    ansatz = RealAmplitudes(num_qubits=8, reps=1)
    param_qc = feature_map.compose(ansatz)
    param_obs = SparsePauliOp("Z" * num_qubits_param)
    param_vals = np.random.rand(param_qc.num_parameters)
    backend = PBackend(num_qubits=8)
    pm = generate_preset_pass_manager(backend=backend, optimization_level=0)
    isa_qc = pm.run(param_qc)
    
    estimator = PyrauliEstimator()
    
    def run_job():
        job = estimator.run([(isa_qc, param_obs, param_vals)])
        job.result()
        
    benchmark(run_job)

def test_qiskit_pbackend_parameterized_zz_real_amp8x8_truncate001_noisy(benchmark):
    np.random.seed(42)
    num_qubits_param = 8
    feature_map = ZZFeatureMap(feature_dimension=num_qubits_param, reps=1)
    ansatz = RealAmplitudes(num_qubits=8, reps=1)
    param_qc = feature_map.compose(ansatz)
    param_obs = SparsePauliOp("Z" * num_qubits_param)
    param_vals = np.random.rand(param_qc.num_parameters)
    backend = PBackend(num_qubits=8)
    pm = generate_preset_pass_manager(backend=backend, optimization_level=0)
    isa_qc = pm.run(param_qc)

    nm = NoiseModel()
    for g in [QGate.X, QGate.Y, QGate.Z, QGate.H, QGate.Rz]:
        nm.add_unital_noise_on_gate(g,UnitalNoise.Depolarizing, 0.01)
    nm.add_unital_noise_on_gate(QGate.Rz, UnitalNoise.Dephasing, 0.01)
    nm.add_amplitude_damping_on_gate(QGate.Cx, 0.05)
    
    estimator = PyrauliEstimator(truncator=CoefficientTruncator(0.01), noise_model=nm)
    
    def run_job():
        job = estimator.run([(isa_qc, param_obs, param_vals)])
        job.result()
        
    benchmark(run_job)
