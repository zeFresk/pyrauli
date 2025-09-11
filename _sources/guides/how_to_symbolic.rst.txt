.. _how_to_symbolic:

Symbolic Simulation
===================

`pyrauli` offers a powerful symbolic simulation mode that allows you to work with parameterized quantum circuits. Instead of providing fixed numerical values for parameters like gate angles or noise strengths, you can use symbolic variables. This is particularly useful for tasks like variational algorithms, gradient calculations, and sensitivity analysis, where you need to explore a function's behavior over a range of parameter values.

The Symbolic Toolkit
--------------------

The symbolic mode is built on three core classes:

* :py:class:`~pyrauli.SymbolicCoefficient`: Represents a mathematical expression that can include variables, constants, and standard mathematical operations.
* :py:class:`~pyrauli.SymbolicObservable`: An observable whose terms have `SymbolicCoefficient` objects as coefficients.
* :py:class:`~pyrauli.SymbolicCircuit`: A circuit that can accept `SymbolicCoefficient` objects as parameters for its operations.

Working with `SymbolicCoefficient`
------------------------------------

The :py:class:`~pyrauli.SymbolicCoefficient` is the fundamental building block. You can create one from a number or a string (which becomes a variable name).

.. literalinclude:: /../tests/snippets/test_symbolic_coefficient_guide.py
   :language: python
   :start-after: # [symbolic_init]
   :end-before: # [symbolic_init]
   :dedent: 4

These objects support standard mathematical operations, allowing you to build complex expressions.

.. literalinclude:: /../tests/snippets/test_symbolic_coefficient_guide.py
   :language: python
   :start-after: # [symbolic_ops]
   :end-before: # [symbolic_ops]
   :dedent: 4

Evaluating Expressions
~~~~~~~~~~~~~~~~~~~~~~

A key feature is the ability to substitute variables with values. There are two ways to do this:

1.  **.evaluate()**: This method substitutes all variables and computes a final floating-point number. It will raise an error if any variables are left unbound.
2.  **.symbolic_evaluate()**: This method substitutes only the specified variables, returning a new, potentially simpler `SymbolicCoefficient`.

.. literalinclude:: /../tests/snippets/test_symbolic_coefficient_guide.py
   :language: python
   :start-after: # [symbolic_evaluate]
   :end-before: # [symbolic_evaluate]
   :dedent: 4

Simplifying Expressions
~~~~~~~~~~~~~~~~~~~~~~~

The :py:meth:`~pyrauli.SymbolicCoefficient.simplified` method applies arithmetic rules (like `x*1=x` or `x+0=x`) to reduce the complexity of an expression.

.. literalinclude:: /../tests/snippets/test_symbolic_coefficient_guide.py
   :language: python
   :start-after: # [symbolic_simplify]
   :end-before: # [symbolic_simplify]
   :dedent: 4

Constructing a `SymbolicObservable`
-------------------------------------

A :py:class:`~pyrauli.SymbolicObservable` works just like a regular :py:class:`~pyrauli.Observable`, but its coefficients are symbolic.

.. literalinclude:: /../tests/snippets/test_symbolic_observable_guide.py
   :language: python
   :start-after: # [symbolic_obs_init]
   :end-before: # [symbolic_obs_init]
   :dedent: 4

The :py:meth:`~pyrauli.SymbolicObservable.simplify` method on an observable will simplify the symbolic coefficients of all its terms. You can also pass a dictionary of variable substitutions to this method.

.. literalinclude:: /../tests/snippets/test_symbolic_observable_guide.py
   :language: python
   :start-after: # [symbolic_obs_simplify]
   :end-before: # [symbolic_obs_simplify]
   :dedent: 4

Building and Running a `SymbolicCircuit`
------------------------------------------

The end-to-end workflow is straightforward. You build a :py:class:`~pyrauli.SymbolicCircuit` using variable names for your parameters and then run it on a :py:class:`~pyrauli.SymbolicObservable`. The simulation propagates the symbolic expressions through the circuit according to the rules of quantum mechanics.

.. literalinclude:: /../tests/snippets/test_symbolic_circuit_snippet.py
   :language: python
   :start-after: # [symbolic_circuit]
   :end-before: # [symbolic_circuit]
   :dedent: 4

The final result is a new :py:class:`~pyrauli.SymbolicObservable`. To get the final expectation value, you call its :py:meth:`~pyrauli.SymbolicObservable.expectation_value` method, which returns a `SymbolicCoefficient`. You can then evaluate this coefficient for any set of concrete parameter values.

.. literalinclude:: /../tests/snippets/test_symbolic_circuit_snippet.py
   :language: python
   :start-after: # [symbolic_evaluation]
   :end-before: # [symbolic_evaluation]
   :dedent: 4

This workflow allows you to run the simulation once to get a general symbolic result and then analyze that result for many different parameter values without needing to re-run the simulation each time.
