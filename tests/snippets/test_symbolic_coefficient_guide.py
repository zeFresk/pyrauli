import pytest

def test_snippet_symbolic_coeff():
    # [symbolic_init]
    from pyrauli import SymbolicCoefficient

    # From a constant
    const_coeff = SymbolicCoefficient(1.23)

    # From a variable name
    var_coeff = SymbolicCoefficient("theta")

    print(const_coeff)
    print(var_coeff)
    # [symbolic_init]

    # [symbolic_ops]
    a = SymbolicCoefficient("a")
    b = SymbolicCoefficient("b")

    # Perform standard arithmetic
    expr = (a * 2 + b) / 3
    print(f"Expression: {expr}")

    # Use trigonometric functions
    trig_expr = expr.cos()
    print(f"Trigonometric Expression: {trig_expr}")
    # [symbolic_ops]

    # [symbolic_evaluate]
    expression = SymbolicCoefficient("a") + SymbolicCoefficient("b")

    # Evaluate fully by providing all variables
    result = expression.evaluate({"a": 2.5, "b": 1.5})
    print(f"Final scalar value: {result}")

    # Partially evaluate by providing only some variables
    partial_result = expression.symbolic_evaluate({"a": 2.5})
    print(f"Partially evaluated expression: {partial_result}")
    # [symbolic_evaluate]


    # [symbolic_simplify]
    x = SymbolicCoefficient("x")

    # Create a redundant expression
    expr = (x * 1 + 0) - (x * 0)
    print(f"Original expression: {expr}")

    # Simplify it
    simplified_expr = expr.simplified()
    print(f"Simplified expression: {simplified_expr}")
    # [symbolic_simplify]
