import pytest

from pyrauli import SymbolicCoefficient, SymbolicObservable

def test_coeff_ops():
    x = SymbolicCoefficient(1.)
    x *= 2.
    x /= 2
    x += 1
    x -= 1
    assert x.evaluate() == 1.

