
.. _observable_guide:

Guide: Using the Observable Primitive
=====================================

The ``Observable`` class is the central data structure in ``pyrauli``. It represents
a quantum observable as a linear combination of Pauli strings.

The Heisenberg Picture
----------------------

``pyrauli`` works in the **Heisenberg picture**, where the quantum state is
considered fixed (as the :math:`|0\rangle^{\otimes n}` state) and the operators
(observables) evolve.

Manual Evolution Example
------------------------

You can manually evolve an observable through a circuit by applying gates in
reverse order. Let's evolve a ``Z`` observable on a two-qubit system through a
Bell state preparation circuit.

.. literalinclude:: ../../tests/snippets/test_observable_evolution.py
   :language: python
   :start-after: # [observable_manual_evolution]
   :end-before: # [observable_manual_evolution]

The final observable is ``XX``. Its expectation value on the initial :math:`|00\rangle` state is 0.

Splitting, Merging, and Truncating
----------------------------------

When working directly with an observable, you are responsible for managing its
complexity.

.. literalinclude:: ../../tests/test_observable.py
   :language: python
   :start-after: def test_truncate():
   :end-before: assert obs.size() == 1
