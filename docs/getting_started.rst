.. _getting_started:

Getting Started
===============

This guide will walk you through installing ``pyrauli`` and running your first
quantum circuit simulation.

Installation
------------

``pyrauli`` requires Python 3.8 or later. You can install it directly from PyPI
using pip.

**Standard Installation**

For core functionality, install the package as follows:

.. code-block:: bash

   pip install pyrauli

**Installation with Qiskit Support**

To use ``pyrauli`` as a Qiskit backend, install it with the ``[qiskit]`` extra:

.. code-block:: bash

   pip install 'pyrauli[qiskit]'


Your First Simulation
---------------------

Let's simulate a simple 2-qubit circuit. This circuit first applies a Hadamard
gate to create a superposition, then entangles the qubits with a CNOT gate.
Finally, we will calculate the expectation value of the :math:`Z \otimes I`
observable.

This example demonstrates the complete basic workflow:

1.  Initialize a ``Circuit``.
2.  Add quantum operations.
3.  Define an ``Observable``.
4.  Run the simulation.
5.  Retrieve the final expectation value.

.. literalinclude:: ../tests/snippets/test_basic_circuit.py
   :language: python
   :start-after: # [basic_circuit]
   :end-before: # [basic_circuit]

This covers the fundamental usage of the ``pyrauli`` library. For more advanced
topics, such as noise modeling, custom policies, and Qiskit integration, please
refer to the detailed guides in the "User Guides" section.
