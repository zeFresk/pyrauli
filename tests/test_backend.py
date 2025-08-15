import pytest
import numpy as np

# Conditional imports for Qiskit and Aer
qiskit = pytest.importorskip("qiskit", minversion="1.0", reason="Qiskit >= 1.0 is required")

from qiskit.circuit import QuantumCircuit, Parameter, ParameterVector
from qiskit.circuit.random import random_circuit
from qiskit.transpiler import generate_preset_pass_manager
from qiskit.quantum_info import SparsePauliOp
from qiskit.primitives import StatevectorEstimator

# Import all necessary components from our package
from pyrauli import PBackend, PyrauliEstimator, NoiseModel, QGate, UnitalNoise

# --- The Final Test Suite ---

def test_backend_initialization_and_target():
    """Tests the PBackend can be initialized and has a valid target."""
    backend = PBackend(num_qubits=4)
    assert backend.name == "pyrauli.PBackend"
    assert backend.target.num_qubits == 4
    assert "h" in backend.target
    assert "cx" in backend.target
    assert "rz" in backend.target

def test_estimator_can_run_simple_circuit():
    """Tests the PyrauliEstimator can run a basic circuit."""
    estimator = PyrauliEstimator()
    qc = QuantumCircuit(1)
    qc.h(0)
    obs = SparsePauliOp("Z") # EV of Z on |+> state is 0
    
    job = estimator.run([(qc, obs)])
    result = job.result()
    assert result[0].data.evs[0] == pytest.approx(0.0)

def p1_to_ev(p1):
        return 1.0 - (2.0 * p1)

def test_estimator_can_run_parameterized_circuit():
    """Tests the estimator with a parameterized circuit."""
    estimator = PyrauliEstimator()
    theta = Parameter('θ')
    qc = QuantumCircuit(1)
    qc.h(0)
    qc.rz(theta, 0)
    qc.h(0)
    obs = SparsePauliOp("Z")
    theta_val = np.pi / 3
    
    job = estimator.run([(qc, obs, [theta_val])])
    result = job.result()
    assert result[0].data.evs[0] == pytest.approx(p1_to_ev(0.25))

def test_estimator_multiple_observables_per_pub():
    """Tests a single circuit against a list of observables in one PUB."""
    estimator = PyrauliEstimator()
    qc = QuantumCircuit(2)
    qc.h([0, 1])
    qc.rz(np.pi/2, 0)
    qc.rz(np.pi/3, 1)
    qc.h([0, 1])
    observables = [SparsePauliOp("ZI"), SparsePauliOp("IZ")]
    
    job = estimator.run([(qc, observables)])
    result = job.result()
    
    expected_evs = [p1_to_ev(0.5), p1_to_ev(0.25)]
    assert result[0].data.evs == pytest.approx(expected_evs, abs=1e-6)


def test_estimator_multiobs_multiparams():
    """Tests a single circuit against a list of observables in one PUB."""
    estimator = PyrauliEstimator()
    thetas = ParameterVector("theta", 2)
    qc = QuantumCircuit(2)
    qc.h([0, 1])
    qc.rz(thetas[0], 0)
    qc.rz(thetas[1], 1)
    qc.h([0, 1])
    observables = [SparsePauliOp("ZI"), SparsePauliOp("IZ")]
    
    job = estimator.run([(qc, observables, (np.pi/2, np.pi/3)), (qc, observables, (np.pi/3, np.pi/2))])
    result = job.result()
    
    assert result[0].data.evs == pytest.approx([p1_to_ev(0.5), p1_to_ev(0.25)], abs=1e-6)
    assert result[1].data.evs == pytest.approx([p1_to_ev(0.25), p1_to_ev(0.5)], abs=1e-6)

def test_noise_model_is_correctly_applied():
    """Confirms the noise model passed to the estimator alters the result."""
    p = 0.1
    noise_model = NoiseModel()
    noise_model.add_unital_noise_on_gate(QGate.H, UnitalNoise.Depolarizing, p)
    estimator = PyrauliEstimator(noise_model=noise_model)
    
    qc = QuantumCircuit(1)
    qc.h(0)
    obs = SparsePauliOp("X") # Noiseless EV is 1.0 for state |0>
    
    job = estimator.run([(qc, obs)])
    result = job.result()
    
    # Depolarizing noise scales the expectation value by (1-p)
    assert result[0].data.evs[0] == pytest.approx(1.0 - p)

def test_transpiler_pass_manager_compatibility():
    """Tests that PBackend's target can be used to create a valid pass manager."""
    backend = PBackend()
    pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
    
    # Circuit with gates not in the basis set
    qc = QuantumCircuit(2)
    qc.rx(np.pi / 2, 0)
    qc.sdg(1)
    
    transpiled_qc = pm.run(qc)
    
    # Check that the circuit was unrolled to the backend's basis gates
    for instruction in transpiled_qc.data:
        assert instruction.operation.name in backend.target

def test_random_circuits_match_aer_simulator():
    """Compares PyrauliEstimator against qiskit for many random circuits."""
    pyrauli_estimator = PyrauliEstimator()
    qiskit_estimator = StatevectorEstimator()
    
    transpilation_backend = PBackend(num_qubits=4)
    pm = generate_preset_pass_manager(backend=transpilation_backend, optimization_level=0)

    np.random.seed(42) # for reproducibility
    for i in range(8):
        qc = random_circuit(num_qubits=4, depth=8, seed=i, max_operands=2)
        obs = SparsePauliOp("Z" * 4)
        transpiled_qc = pm.run(qc)
        
        # Run on pyrauli
        pyrauli_job = pyrauli_estimator.run([(transpiled_qc, obs)])
        pyrauli_result = pyrauli_job.result()[0].data.evs[0]
        
        # Run on Aer
        qiskit_job = qiskit_estimator.run([(transpiled_qc, obs)])
        qiskit_result = qiskit_job.result()
        qiskit_ev = qiskit_result[0].data.evs #.... 
        
        assert pyrauli_result == pytest.approx(qiskit_ev, abs=1e-6)
