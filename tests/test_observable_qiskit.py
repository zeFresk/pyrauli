import pytest
from pyrauli import (
    Observable,
    PauliTerm,
    PauliGate,
    CliffordGate,
    CoefficientTruncator,
    UnitalNoise,
)
from math import pi

# --- Optional Qiskit Integration Tests ---
qiskit = pytest.importorskip("qiskit", reason="Qiskit extra not installed")
from pyrauli import from_qiskit
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
