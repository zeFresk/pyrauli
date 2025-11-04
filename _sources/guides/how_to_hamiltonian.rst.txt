.. _how_to_hamiltonian:

Simulate Hamiltonian Time Evolution
===================================

A key task in quantum simulation is calculating the time evolution of a system
under a given Hamiltonian, ``H``. ``pyrauli`` is exceptionally well-suited for this
task when the Hamiltonian can be expressed as a single, multi-qubit Pauli string
(e.g., ``H = XZIX``), which is common in physics models and algorithm building blocks.

This is because the evolution operator, :math:`U(t) = e^{-iHt}`, can be applied
directly to the observable in the Heisenberg picture without needing to be
decomposed into a complex sequence of one- and two-qubit gates.

The `eiht` Gate: Your Primary Tool
----------------------------------

The primary method for Hamiltonian evolution is :py:meth:`~pyrauli.Circuit.eiht`.
It directly applies the evolution operator for a given time ``t``.

.. code-block:: python

   circuit.eiht(pauli_axis, t)

* ``pauli_axis``: A list of strings defining the Pauli operators in the Hamiltonian term (e.g., ``["X", "Z", "I", "X"]``).
* ``t``: A float representing the evolution time.

The following example simulates an 8-qubit system evolving under a 4-local
**Wen Plaquette** operator, :math:`H = X_0 Z_1 X_4 Z_5`. We then measure the
expectation value of the :math:`Z_0` observable.

.. literalinclude:: /../tests/snippets/test_hamiltonian_guide.py
   :language: python
   :start-after: # [eiht_basic_usage]
   :end-before: # [eiht_basic_usage]
   :dedent: 4

The `Rp` Gate vs. `eiht`
------------------------

``pyrauli`` also provides the :py:meth:`~pyrauli.Circuit.rp` gate, which applies
a generalized rotation around a Pauli axis. It is important to understand the
distinction between the two:

* :py:meth:`~pyrauli.Circuit.eiht` implements the standard physics definition of time evolution: :math:`U = e^{-i P t}`.
* :py:meth:`~pyrauli.Circuit.rp` implements the standard quantum gate rotation: :math:`U = e^{-i P \theta / 2}`.

This leads to a simple relationship between their parameters: a time evolution
for time ``t`` is equivalent to a rotation by an angle ``theta = 2*t``.

.. tip::
   **`circuit.eiht(axis, t)`** is equivalent to **`circuit.rp(axis, 2 * t)`**.

The following code provides a concrete demonstration of this equivalence.

.. literalinclude:: /../tests/snippets/test_hamiltonian_guide.py
   :language: python
   :start-after: # [rp_vs_eiht]
   :end-before: # [rp_vs_eiht]
   :dedent: 4

Symbolic Time Evolution
-----------------------

A powerful feature of ``pyrauli`` is that the time parameter ``t`` can be a
symbolic variable. This allows you to run the simulation just *once* to obtain
a symbolic expression for an expectation value as a function of time. You can
then evaluate this expression for any number of time points without re-running
the simulation.

This is ideal for analyzing the dynamics of a system or for algorithms where
time is a parameter to be optimized.

.. literalinclude:: /../tests/snippets/test_hamiltonian_guide.py
   :language: python
   :start-after: # [symbolic_evolution]
   :end-before: # [symbolic_evolution]
   :dedent: 4
