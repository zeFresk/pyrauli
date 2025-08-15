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

.. code-block:: python

   from pyrauli import Observable, CliffordGate

   # Start with a Z observable on the first of two qubits
   obs = Observable("ZI")
   print(f"Initial observable: {obs}")

   # Evolve the observable backward through a CNOT gate
   obs.apply_cx(0, 1)
   print(f"After CX(0,1):      {obs}")

   # Evolve backward through an H gate on qubit 0
   obs.apply_clifford(CliffordGate.H, 0)
   print(f"After H(0):         {obs}")

Splitting, Merging, and Truncating
----------------------------------

When working directly with an observable, you are responsible for managing its
complexity.

.. literalinclude:: ../../pyrauli/tests/test_observable.py
   :language: python
   :start-after: def test_truncate():
   :end-before: assert obs.size() == 1
