.. _how_to_circuits:

How-To: Build and Run Circuits
==============================

This guide provides recipes for the primary workflow in ``pyrauli``: building a
``Circuit`` object and using it to evolve an ``Observable``.

Construct a Basic Circuit
-------------------------

The ``Circuit`` class is the main entry point. You initialize it with the
number of qubits and then add gates sequentially. Finally you run the circuit on a target Observable.

.. literalinclude:: /../tests/snippets/test_basic_circuit.py
   :language: python
   :start-after: # [basic_circuit]
   :end-before: # [basic_circuit]
   :dedent: 4


