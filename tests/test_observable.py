import pytest
from pyrauli import Observable, PauliTerm, PauliGate, from_qiskit


def test_observable_init_string():
    obs = Observable("IIII")
    assert obs == Observable("IIII", 1)


def test_observable_init_multistring():
    obs = Observable(["IIII", "XXXX"])
    assert obs.size() == 2
    assert obs[0] == PauliTerm("IIII")
    assert obs[1] == PauliTerm("XXXX")


def test_observable_init_pts():
    pt1 = PauliTerm("IX", -0.3)
    pt2 = PauliTerm("XI", 0.5)
    obs = Observable([pt1, pt2])
    assert obs.size() == 2
    assert obs[0] == pt1
    assert obs[1] == pt2

def test_empty_observable_not_allowed():
    with pytest.raises(ValueError):
        obs = Observable("")

def test_mismatched_pt_not_allowed():
    with pytest.raises(ValueError):
        obs = Observable(["I", "XI"])

def test_observable_apply_pauli():
    obs = Observable("ZX")
    obs.apply_pauli(PauliGate.X, 0)


# --- Optional Qiskit Integration Tests ---
qiskit = pytest.importorskip("qiskit", reason="Qiskit extra not installed")
from qiskit.quantum_info import SparsePauliOp


def test_observable_from_SparsePauliOp_basic():
    qobs = SparsePauliOp("IZ")
    pobs = from_qiskit(qobs)
    assert pobs == Observable("IZ")


def test_observable_from_SparsePauliOp_hard():
    qobs = SparsePauliOp.from_list([("XIIZI", 1), ("IYIIY", 2)])
    pobs = from_qiskit(qobs)
    assert pobs.size() == 2
    assert pobs[0] == PauliTerm("XIIZI")
    assert pobs[1] == PauliTerm("IYIIY", 2)
