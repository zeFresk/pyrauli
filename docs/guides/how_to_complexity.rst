.. _how_to_complexity:

Manage Simulation Complexity
============================

As a simulation progresses, the number of terms in an :py:class:`~pyrauli.Observable` can grow
exponentially, making the simulation slow or memory-intensive. ``pyrauli``
provides powerful tools (:py:class:`~pyrauli.Truncator` and :py:class:`~pyrauli.SchedulingPolicy` objects) to
manage this complexity automatically during a :py:class:`~pyrauli.Circuit.run()` call.


Remove small coefficients
-------------------------

**Solution:** Use a :py:class:`~pyrauli.CoefficientTruncator`.

This truncator removes any Pauli terms whose coefficient magnitude is below a
given threshold.

.. literalinclude:: /../tests/test_truncator.py
   :language: python
   :start-after: # [truncator_coeff]
   :end-before: # [truncator_coeff]
   :dedent: 4

Using a custom Truncator with your own logic
--------------------------------------------

**Solution:** Use a :py:class:`~pyrauli.LambdaTruncator`.

This allows you to provide a custom Python function that filters the terms.

.. literalinclude:: /../tests/test_truncator.py
   :language: python
   :start-after: # [truncator_lambda]
   :end-before: # [truncator_lambda]
   :dedent: 4

.. NOTE::
   This truncator removes :py:class:`~pyrauli.PauliTerm` containing :math:`Y`. However, this is not an efficient.

Controlling when truncation is applied
--------------------------------------

**Solution:** Use a :py:class:`~pyrauli.SchedulingPolicy`.

Scheduling Policies give you fine-grained control over when a :py:class:`~pyrauli.Truncator` is
applied during the simulation. It can query a :py:class:`~pyrauli.SimulationState` object and other information to make a decision.

The following example uses a :py:class:`~pyrauli.LambdaPolicy`
to apply a truncator only at specific depths.

.. literalinclude:: /../tests/test_policies.py
   :language: python
   :start-after: # [policy_lambda]
   :end-before: # [policy_lambda]
   :dedent: 4

.. NOTE::
   See :py:class:`~pyrauli.SimulationState`, :py:class:`~pyrauli.OperationType`, :py:class:`~pyrauli.Timing` and :py:class:`~pyrauli.LambdaPolicy` for more information.

