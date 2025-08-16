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


def test_apply_pauli():
    obs = Observable("ZX")
    obs.apply_pauli(PauliGate.X, 0)


def test_apply_clifford():
    obs = Observable("ZX")
    obs.apply_clifford(CliffordGate.H, 0)


def test_apply_cx():
    obs = Observable("ZX")
    obs.apply_cx(0, 1)
    obs.apply_cx(1, 0)


def test_apply_rz():
    obs = Observable("ZX")
    obs.apply_rz(0, pi / 2)


def test_apply_amplitude_damping():
    obs = Observable("ZX")
    obs.apply_amplitude_damping(1, 0.01)


def test_apply_unital_noise_depolarizing():
    obs = Observable("ZX")
    obs.apply_unital_noise(UnitalNoise.Depolarizing, 0, 0.01)


def test_apply_unital_noise_dephazing():
    obs = Observable("ZX")
    obs.apply_unital_noise(UnitalNoise.Dephasing, 0, 0.01)


def test_ev():
    obs = Observable("Z")
    obs.apply_clifford(CliffordGate.H, 0)
    obs.apply_rz(0, pi / 3)
    obs.apply_clifford(CliffordGate.H, 0)
    assert obs.expectation_value() == pytest.approx(0.5)


def test_merge():
    obs = Observable(["IZ", "IZ"])
    obs.merge()
    assert obs.size() == 1
    assert obs[0].coefficient == pytest.approx(2.0)


def test_truncate():
    # [test_truncate]
    obs = Observable([PauliTerm("II", 0.999), PauliTerm("ZZ", 0.001)])
    truncator = CoefficientTruncator(0.01)
    obs.truncate(truncator)
    assert obs.size() == 1
    # [test_truncate]
    assert obs[0] == PauliTerm("II", 0.999)


def test_bad_op_not_allowed():
    obs = Observable("ZZ")
    with pytest.raises(ValueError):
        obs.apply_pauli(PauliGate.X, 2)
    with pytest.raises(ValueError):
        obs.apply_clifford(CliffordGate.H, 2)
    with pytest.raises(ValueError):
        obs.apply_cx(0, 2)
    with pytest.raises(ValueError):
        obs.apply_cx(2, 0)
    with pytest.raises(ValueError):
        obs.apply_cx(0, 0)
    with pytest.raises(ValueError):
        obs.apply_rz(2, pi / 2)
    with pytest.raises(ValueError):
        obs.apply_amplitude_damping(2, 0.01)
    with pytest.raises(ValueError):
        obs.apply_unital_noise(UnitalNoise.Depolarizing, 2, 0.01)


def test_len():
    assert len(Observable(["II", "XX"])) == 2
