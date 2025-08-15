.. _circuit_guide:

Guide: Building Quantum Circuits
================================

The ``Circuit`` class is the primary high-level interface for constructing
and simulating quantum circuits.

Basic Circuit Construction
--------------------------

.. literalinclude:: ../../pyrauli/README.md
   :language: python
   :start-after: ### Core Usage
   :end-before: print(f"Expectation value of ZI: {final_observable.expectation_value()}")

Managing Complexity with Truncators
-----------------------------------

``pyrauli`` provides built-in truncators to manage simulation complexity.

.. literalinclude:: ../../pyrauli/tests/test_truncator.py
   :language: python
   :start-after: def test_coefficient_truncator_on_observable():
   :end-before: assert obs[0] == PauliTerm("I", 0.99)

Custom Truncators with `LambdaTruncator`
----------------------------------------

You can define custom truncation logic using `LambdaTruncator`.

.. literalinclude:: ../../pyrauli/tests/test_truncator.py
   :language: python
   :start-after: def test_lambda_truncator_on_observable_def():
   :end-before: assert obs[0] == PauliTerm("IXI", 0.5)

Controlling Optimization with Scheduling Policies
-------------------------------------------------

Scheduling Policies give you fine-grained control over *when* optimizations
are applied.

.. literalinclude:: ../../pyrauli/tests/test_policies.py
   :language: python
   :start-after: def test_lambda_policy_in_circuit():
   :end-before: assert len(obs_out) == 2
