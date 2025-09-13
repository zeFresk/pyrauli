import pytest
from pyrauli import (
    SymbolicObservable,
    SymbolicCoefficient,
    SymbolicPauliTerm,
    SymbolicWeightTruncator,
    PauliGate,
    CliffordGate,
    UnitalNoise,
)
from math import pi


def test_init():
    SymbolicObservable("IXYZ")
    SymbolicObservable("IXYZ", SymbolicCoefficient("a"))
    SymbolicObservable(["IXYZ", "ZZZZ"])
    SymbolicObservable([SymbolicPauliTerm("X", "a"), SymbolicPauliTerm("Z", "b")])


def test_apply_pauli():
    obs = SymbolicObservable("X")
    obs.apply_pauli(PauliGate.Z, 0)
    assert str(obs[0]) == "-1 X"


def test_apply_clifford():
    obs = SymbolicObservable("X")
    obs.apply_clifford(CliffordGate.H, 0)
    assert str(obs[0]) == "1 Z"


def test_apply_cx():
    obs = SymbolicObservable("IX")
    obs.apply_cx(0, 1)
    assert str(obs[0]) == "1 IX"


def test_apply_rz():
    obs = SymbolicObservable("X")
    obs.apply_rz(0, "theta")
    assert obs.size() == 2
    assert str(obs[0]) == "1 * cos(theta) X"
    assert str(obs[1]) == "1 * -(sin(theta)) Y"


def test_apply_unital_noise():
    obs = SymbolicObservable("X")
    obs.apply_unital_noise(UnitalNoise.Depolarizing, 0, "p")
    assert str(obs[0].coefficient.simplified()) == "1 - p"


def test_apply_amplitude_damping():
    obs = SymbolicObservable("Z")
    obs.apply_amplitude_damping(0, "p")
    assert obs.size() == 2


def test_expectation_value():
    obs = SymbolicObservable("Z")
    assert obs.expectation_value().evaluate() == 1
    obs = SymbolicObservable("X", "a")
    assert obs.expectation_value().evaluate({"a": 1}) == 0


def test_merge():
    obs = SymbolicObservable([SymbolicPauliTerm("X", "a"), SymbolicPauliTerm("X", "a")])
    obs.merge()
    obs.simplify()
    assert obs.size() == 1
    assert obs[0].coefficient.to_string() == "2.000 * a"


def test_truncate():
    obs = SymbolicObservable([SymbolicPauliTerm("X", 0.1), SymbolicPauliTerm("Y", 0.9)])
    truncator = SymbolicWeightTruncator(0)  # Removes all non-identity
    obs.truncate(truncator)
    assert obs.size() == 0


def test_simplify():
    obs = SymbolicObservable([SymbolicPauliTerm("X", "a"), SymbolicPauliTerm("X", 1.0)])
    obs.merge()
    assert obs[0].coefficient.to_string() == "a + 1.000"
    obs.simplify()
    assert obs[0].coefficient.to_string() == "1.000 + a"  # No change
    obs.simplify({"a": 2.0})
    assert obs[0].coefficient.to_string() == "3.000"
