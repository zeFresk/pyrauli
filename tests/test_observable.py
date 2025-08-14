import pytest 
from pyrauli import Observable, PauliTerm, Pauli  

def test_observable_init_string():
    obs = Observable("IIII")
    assert obs == Observable("IIII", 1)

def test_observable_init_multistring():
    obs = Observable(["IIII", "XXXX"])
    assert obs.size() == 2
