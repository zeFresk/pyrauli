# tests/snippets/test_symbolic_sympy.py
from pyrauli import SymbolicCircuit, SymbolicObservable
import pytest

sympy = pytest.importorskip("sympy", reason="symbolic extra not installed")

def test_sympy_snippet():
    # [symbolic_sympy]
    # Create and run a symbolic circuit as before
    circuit = SymbolicCircuit(1)
    circuit.add_operation("H", 0)
    circuit.add_operation("Rz", 0, "theta")
    circuit.add_operation("H", 0)
    observable = SymbolicObservable("Z")
    final_observable = circuit.run(observable)
    symbolic_coeff = final_observable.expectation_value()

    # Convert to a SymPy expression
    sympy_expr = symbolic_coeff.to_sympy()

    # Now you can use SymPy's features
    theta = sympy.Symbol("theta")
    print(sympy.diff(sympy_expr, theta))
    # [symbolic_sympy]
