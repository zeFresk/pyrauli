.. _how_to_qiskit:

Integrate with Qiskit
=====================

``pyrauli`` offers seamless integration with Qiskit. This guide provides
recipes for common integration tasks.

Convert Qiskit objects to ``pyrauli`` objects
---------------------------------------------

The :py:class:`~pyrauli.from_qiskit` function converts Qiskit ``QuantumCircuit`` and ``SparsePauliOp`` objects to their ``pyrauli`` equivalents.

.. literalinclude:: /../tests/test_circuit_qiskit.py
   :language: python
   :start-after: # [from_qiskit]
   :end-before: # [from_qiskit]
   :dedent: 4

.. WARNING::
   :py:func:`~pyrauli.from_qiskit` only works if your circuit doesn't require transpilation (i.e. only use gates compatible with :py:class:`~pyrauli.Circuit`). For more complex circuits, refer to the section below.

Use ``pyrauli`` as a Qiskit-compatible backend
----------------------------------------------

The :py:class:`~pyrauli.PBackend` class allows you to use ``pyrauli`` as a backend within the
Qiskit ecosystem, enabling you to **transpile** and run circuits defined in Qiskit on the
``pyrauli`` simulator.

Here is an example of transpilation to :py:class:`~pyrauli.PBackend`, relying on Qiskit ``PassManager``:

.. literalinclude:: /../tests/test_backend.py
   :language: python
   :start-after: # [qiskit_backend_transpilation]
   :end-before: # [qiskit_backend_transpilation]
   :dedent: 4

And how to run it on the backend:

.. literalinclude:: /../tests/test_backend.py
   :language: python
   :start-after: # [qiskit_backend_run]
   :end-before: # [qiskit_backend_run]
   :dedent: 4

Note that at this stage you could also call :py:class:`~pyrauli.from_qiskit` on `transpiled_qc` directly.

Use the :py:class:`~pyrauli.PyrauliEstimator` Qiskit Primitive
--------------------------------------------------------------

For modern, algorithm-focused development, the :py:class:`~pyrauli.PyrauliEstimator` provides a ``BaseEstimatorV2`` primitive that uses the ``pyrauli`` simulator under
the hood.

.. literalinclude:: /../tests/test_backend.py
   :language: python
   :start-after: # [estimator_complex]
   :end-before: # [estimator_complex]
   :dedent: 4
