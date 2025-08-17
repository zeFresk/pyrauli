.. _how_to_circuits:

Build and Run Circuits
======================

This guide provides recipes for the primary workflow in ``pyrauli``: building a
:py:class:`~pyrauli.Circuit` object and using it to evolve an :py:class:`~pyrauli.Observable`.

Construct a Basic Circuit
-------------------------

The :py:class:`~pyrauli.Circuit` class is the main entry point. You initialize it with the
number of qubits and then add gates sequentially. Finally, you run the circuit on a target Observable.

.. literalinclude:: /../tests/snippets/test_basic_circuit.py
   :language: python
   :start-after: # [basic_circuit]
   :end-before: # [basic_circuit]
   :dedent: 4


