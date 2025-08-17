.. _getting_started:

Getting started: Your First Simulation
======================================

In this tutorial, you will learn the complete, end-to-end workflow for
simulating a quantum circuit with ``pyrauli``. We will build a Bell state, one
of the most fundamental entangled states in quantum computing, and measure a
property of it.

By the end, you will understand how to construct circuits, define observables,
and interpret the results of a simulation that uses the Heisenberg picture.

Installation
------------

``pyrauli`` requires Python 3.9 or later. You can install it directly from PyPI
using pip.

**Standard Installation**

For core functionality, install the package as follows:

.. code-block:: bash

   pip install pyrauli

**Installation with Qiskit Support**

To use ``pyrauli`` as a Qiskit backend, install it with the ``[qiskit]`` extra:

.. code-block:: bash

   pip install 'pyrauli[qiskit]'


Simulating a Bell State
-----------------------

Let's simulate a 2-qubit circuit that prepares a Bell state. This circuit first
applies a Hadamard gate to create a superposition, then entangles the qubits
with a CNOT gate. Finally, we will calculate the expectation value of the
:math:`Z \otimes I` observable.

This example demonstrates the complete basic workflow:

1.  **Initialize a** :py:class:`~pyrauli.Circuit`: We start by defining the number of qubits our
    circuit will have.

2.  **Add quantum operations**: We add gates to the circuit in the order they
    should be applied.

3.  **Define an** :py:class:`~pyrauli.Observable`: We specify the physical quantity we want to
    measure at the end of the computation.

4.  **Run the simulation**: This is where ``pyrauli``'s unique approach comes
    into play. Instead of evolving the state, we evolve the observable.

5.  **Retrieve the final expectation value**: We calculate the expectation
    value of the *final, evolved observable* with respect to the initial
    :math:`|00...0\rangle` state.

Here is the complete code:

.. literalinclude:: /../tests/snippets/test_basic_circuit.py
   :language: python
   :start-after: # [basic_circuit]
   :end-before: # [basic_circuit]
   :dedent: 4

**Dissecting the Simulation**

Let's look at the key lines more closely.

.. code-block:: python

   observable = pyrauli.Observable("ZI")

Here, we define the physical quantity we want to measure. The string ``"ZI"`` tells ``pyrauli`` that we are interested in the Pauli-Z operator acting on qubit 0 and the identity operator acting on all other qubits (in this case, qubit 1). 

In the standard Schrödinger picture, this would be the measurement we perform at the *end* of the circuit. In the Heisenberg picture used by ``pyrauli``, this observable is our starting point.

.. code-block:: python

   final_observable = circuit.run(observable)

This is the core of the ``pyrauli`` simulation. Instead of evolving a state vector forward through the circuit, the :py:class:`~pyrauli..run()` method evolves our *observable* backward. 
The :py:class:`~pyrauli.final_observable` represents what our initial observable ``ZI`` becomes after being transformed by all the gates in the circuit.

.. code-block:: python

   expectation_value = final_observable.expectation_value()

The final step is to calculate the expectation value of this transformed
observable with respect to the simple, known initial state of all qubits in
the :math:`|0\rangle` state. The result, ``0.0``, is the same value you would
get from a statevector simulation.

Next Steps
----------

You now have a foundational understanding of the ``pyrauli`` workflow. To learn
how to solve specific problems, head to our :doc:`../guides/how_to_circuit`.
To understand the theory behind the Heisenberg picture and Pauli
back-propagation, see our :doc:`../explanation/theory`.
