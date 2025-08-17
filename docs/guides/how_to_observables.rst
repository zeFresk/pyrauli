.. _how_to_observables:

Work with Observables
=====================

This guide covers direct manipulation of :py:class:`~pyrauli.Observable` objects.

Manually Evolve an Observable
-----------------------------

While the :py:class:`~pyrauli.Circuit.run()` method is the easiest way to perform a simulation,
you can also apply gate transformations directly to an :py:class:`~pyrauli.Observable` object.
This can be useful for debugging or custom simulation flows.

.. WARNING::
   Due to Python overhead, using :py:class:`~pyrauli.Observable` apply methods instead of running a circuit can be up to :math:`1000` times slower.

Note that you must apply the gates in reverse order to match the definition of
Heisenberg evolution.

.. literalinclude:: /../tests/snippets/test_observable_evolution.py
   :language: python
   :start-after: # [observable_manual_evolution]
   :end-before: # [observable_manual_evolution]
   :dedent: 4

Manage Observable Complexity
----------------------------

When an observable is evolved, the number of Pauli terms it contains can grow.
You can manually truncate an observable to keep only the most significant
terms. The following example keeps only the term with the largest coefficient.

.. literalinclude:: /../tests/test_observable.py
   :language: python
   :start-after: # [test_truncate]
   :end-before: assert obs.size() == 1
   :dedent: 4

.. NOTE::
   See :ref:`how_to_complexity`, for more information on :py:class:`~pyrauli.Truncator`.
