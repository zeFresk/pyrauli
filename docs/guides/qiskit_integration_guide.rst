.. _qiskit_integration_guide:

Guide: Qiskit Integration
=========================

``pyrauli`` offers a seamless integration with Qiskit, allowing you to use
it as a backend for your Qiskit circuits.

`from_qiskit`: Converting Qiskit Objects
----------------------------------------

The `from_qiskit` function converts Qiskit `QuantumCircuit` and `SparsePauliOp`
objects to their `pyrauli` equivalents.

.. literalinclude:: ../../tests/test_circuit.py
   :language: python
   :start-after: def test_from_qiskit_bell_state():
   :end-before: assert result_manual == result_converted

`PBackend`: The Qiskit-Compatible Backend
-----------------------------------------

`PBackend` allows you to use `pyrauli` as a Qiskit backend.

.. literalinclude:: ../../tests/snippets/test_qiskit_backend_usage.py
   :language: python
   :start-after: # [qiskit_backend_usage]
   :end-before: # [qiskit_backend_usage]


`PyrauliEstimator`: A Qiskit Primitive
---------------------------------------

The `PyrauliEstimator` is a Qiskit `BaseEstimatorV2` primitive that uses the
`pyrauli` simulator.

.. literalinclude:: ../../tests/test_backend.py
   :language: python
   :start-after: def test_estimator_can_run_simple_circuit():
   :end-before: assert result[0].data.evs[0] == pytest.approx(0.0)
