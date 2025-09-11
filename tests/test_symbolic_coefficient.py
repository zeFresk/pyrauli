import pytest
from pyrauli import SymbolicCoefficient
from math import pi, cos, sin, sqrt
import sympy


def test_init():
    assert SymbolicCoefficient(1.0).to_string() == "1.000"
    assert SymbolicCoefficient("x").to_string() == "x"


def test_to_string():
    assert SymbolicCoefficient(1.234567).to_string("{:.2f}") == "1.23"
    x = SymbolicCoefficient("x")
    expr = x * 2 + 3
    assert expr.to_string() == "(x * 2.000) + 3.000"


def test_evaluate():
    assert SymbolicCoefficient(1.0).evaluate() == 1.0
    x = SymbolicCoefficient("x")
    with pytest.raises(ValueError):
        x.evaluate()  # Test for unbound variable
    assert x.evaluate({"x": 2.0}) == 2.0


def test_symbolic_evaluate():
    x = SymbolicCoefficient("x")
    y = SymbolicCoefficient("y")
    expr = x + y
    new_expr = expr.symbolic_evaluate({"x": 1})
    assert new_expr.to_string() == "1.000 + y"
    assert new_expr.evaluate({"y": 2}) == 3


def test_unary_ops():
    x = SymbolicCoefficient("x")
    assert (-x).evaluate({"x": 1}) == -1
    assert x.cos().evaluate({"x": 0}) == cos(0)
    assert x.sin().evaluate({"x": pi / 2}) == sin(pi / 2)
    assert x.sqrt().evaluate({"x": 4}) == sqrt(4)


def test_binary_ops():
    x = SymbolicCoefficient("x")
    y = SymbolicCoefficient("y")
    assert (x + y).evaluate({"x": 1, "y": 2}) == 3
    assert (x - 3).evaluate({"x": 1}) == -2
    assert (x * y).evaluate({"x": 2, "y": 3}) == 6
    assert (4 / y).evaluate({"y": 2}) == 2


def test_long_expression():
    x = SymbolicCoefficient("x")
    y = SymbolicCoefficient("y")
    expr = 2 * (x + y) - (x / 3)
    assert expr.evaluate({"x": 3, "y": 1}) == pytest.approx(7.0)


def test_simplified():
    x = SymbolicCoefficient("x")
    expr = (x + 0) * 1
    simplified_expr = expr.simplified()
    assert simplified_expr.to_string() == "x"


def test_to_sympy():
    x = SymbolicCoefficient("x")
    y = SymbolicCoefficient("y")
    expr = 2 * (x + y)
    sympy_expr = expr.to_sympy()

    sx = sympy.Symbol("x")
    sy = sympy.Symbol("y")

    assert str(sympy_expr) == "2.0*x + 2.0*y"
