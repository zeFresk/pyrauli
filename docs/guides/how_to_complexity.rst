.. _how_to_complexity:

How-To: Manage Simulation Complexity
====================================

As a simulation progresses, the number of terms in an ``Observable`` can grow
exponentially, making the simulation slow or memory-intensive. ``pyrauli``
provides powerful tools (``Truncator`` and ``SchedulingPolicy`` objects) to
manage this complexity automatically during a ``Circuit.run()`` call.


Remove small coefficients
-------------------------

**Solution:** Use a ``CoefficientTruncator``.

This truncator removes any Pauli terms whose coefficient magnitude is below a
given threshold.

.. literalinclude:: /../tests/test_truncator.py
   :language: python
   :start-after: # [truncator_coeff]
   :end-before: # [truncator_coeff]
   :dedent: 4

Using a custom Truncator with your own logic
--------------------------------------------

**Solution:** Use a ``LambdaTruncator``.

This allows you to provide a custom Python function that filters the terms.

.. literalinclude:: /../tests/test_truncator.py
   :language: python
   :start-after: # [truncator_lambda]
   :end-before: # [truncator_lambda]
   :dedent: 4

.. NOTE::
   This truncator removes ``PauliTerm`` containing :math:`Y`. However, this is not an efficient.

Controlling when truncation is applied
--------------------------------------

**Solution:** Use a ``SchedulingPolicy``.

Scheduling Policies give you fine-grained control over when a ``Truncator`` is
applied during the simulation. It can query a ``SimulationState`` object and other information to make a decision.

The following example uses a ``LambdaPolicy``
to apply a truncator only at specific depths.

.. literalinclude:: /../tests/test_policies.py
   :language: python
   :start-after: # [policy_lambda]
   :end-before: # [policy_lambda]
   :dedent: 4

.. NOTE::
   See ``SimulationState``, ``OperationType``, ``Timing`` and ``LambdaPolicy`` for more information.

