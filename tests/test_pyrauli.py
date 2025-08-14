import pytest
import pyrauli
import math
import numpy as np

# --- Core pyrauli Tests ---

def test_circuit_creation():
    """Tests that a pyrauli.Circuit can be created."""
    qc = pyrauli.Circuit(4)
    assert qc.nb_qubits() == 4

def test_add_operations():
    """Tests that operations can be added without errors."""
    qc = pyrauli.Circuit(2)
    qc.add_operation("H", 0)
    qc.add_operation("CX", 0, 1)
    qc.add_operation("Rz", 1, math.pi / 4)

def test_run_simple_circuit():
    """Tests a simple circuit run and expectation value."""
    qc = pyrauli.Circuit(1)
    qc.add_operation("H", 0)
    observable = pyrauli.Observable("Z")
    final_observable = qc.run(observable)
    # After H, Z becomes X. Expectation value of X on |+> is 1, but on |0> it's 0.
    # The initial state is implicitly |0>, so the observable evolves.
    # HZH = X. The expectation value of X on the |0> state is 0.
    assert final_observable.expectation_value() == pytest.approx(0.0)

def test_pauli_term():
    """Tests basic PauliTerm functionality."""
    pt = pyrauli.PauliTerm("IXYZ", 0.5)
    assert pt.coefficient == 0.5
    assert len(pt) == 4

def test_observable():
    """Tests basic Observable functionality."""
    obs = pyrauli.Observable(["IX", "ZY"])
    assert len(obs) == 2

# --- Optional Qiskit Integration Tests ---

# Mark the entire block of tests to be skipped if qiskit is not found.
# pytest.importorskip will skip the test if the import fails.
qiskit = pytest.importorskip("qiskit", reason="Qiskit extra not installed")
from qiskit.circuit import QuantumCircuit, Parameter
from qiskit.quantum_info import SparsePauliOp
from qiskit.primitives import StatevectorEstimator

def test_qiskit_backend_bell_state():
    """Tests the PBackend with a simple Bell state circuit."""
    from pyrauli.backend import PBackend

    qc_bell = QuantumCircuit(2)
    qc_bell.h(0)
    qc_bell.cx(0, 1)

    obs_z = SparsePauliOp("ZI")
    obs_x = SparsePauliOp("XI")

    backend = PBackend()
    bell_pub = (qc_bell, [obs_z, obs_x])
    job = backend.run([bell_pub])
    result = job.result()
    exp_values = result[0].data.evs

    result_qiskit = StatevectorEstimator().run([bell_pub]).result()
    ev_qiskit = result_qiskit[0].data.evs

    # For a Bell state |Φ+⟩ = (|00⟩ + |11⟩)/√2:
    # ⟨Φ+|ZI|Φ+⟩ = 0
    # ⟨Φ+|XI|Φ+⟩ = 1
    assert exp_values[0] == pytest.approx(ev_qiskit[0])
    assert exp_values[1] == pytest.approx(ev_qiskit[1])
    assert exp_values == pytest.approx(ev_qiskit)

def test_qiskit_backend_parameterized():
    """Tests the PBackend with a parameterized circuit."""
    from pyrauli.backend import PBackend

    theta = Parameter('θ')
    qc_param = QuantumCircuit(1)
    qc_param.h(0)
    qc_param.rz(theta, 0)

    obs_y = SparsePauliOp("Y")
    
    theta_val = np.pi / 2
    param_pub = (qc_param, obs_y, [theta_val])
    
    backend = PBackend()
    job = backend.run([param_pub])
    result = job.result()
    exp_val = result[0].data.evs[0]
    
    result_qiskit = StatevectorEstimator().run([param_pub]).result()
    ev_qiskit = result_qiskit[0].data.evs

    assert exp_val == pytest.approx(ev_qiskit)
    assert exp_val == pytest.approx(1.0)
