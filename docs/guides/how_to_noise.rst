.. _how_to_noise:

Simulate Noisy Circuits
=======================

Quantum computations are susceptible to noise from the environment, which can introduce errors and alter results. ``pyrauli`` provides a comprehensive ``NoiseModel`` class to simulate the effects of various noise channels on your quantum circuits. This guide demonstrates how to apply noise models when working with ``Circuit`` objects directly, or when using ``pyrauli`` as a backend within Qiskit via ``PBackend`` and ``PyrauliEstimator``.

Apply Noise to a ``pyrauli`` Circuit
------------------------------------

You can introduce noise into a simulation by creating a ``NoiseModel`` and associating it with a ``Circuit``. The noise model is applied automatically.

.. literalinclude:: /../tests/test_noise_model.py
   :language: python
   :start-after: # [noisy_circuit]
   :end-before: # [noisy_circuit]
   :dedent: 4

The Importance of Truncation with Noise
---------------------------------------

Noise models, especially those that split a single Pauli term into multiple terms (like amplitude damping), can cause the number of terms in an ``Observable`` to grow rapidly. Without management, this can quickly make the simulation intractable.

To counteract this, it is crucial to use a ``Truncator`` with an appropriate ``SchedulingPolicy`` when running noisy simulations. This will prune terms that are unlikely to contribute significantly to the final expectation value, keeping the simulation feasible.

The example below shows how to configure a circuit to apply a ``CoefficientTruncator`` after every gate that splits the observable, ensuring the complexity remains under control.

.. literalinclude:: /../tests/test_truncator.py
   :language: python
   :start-after: # [truncator_coefficient]
   :end-before: # [truncator_coefficient]
   :dedent: 4

.. NOTE::
   See :ref:`how_to_complexity` for more information on using ``Truncator``.

Use Noise Models with Qiskit Backends
-------------------------------------

When using ``pyrauli`` as a backend within the Qiskit ecosystem, you can specify noise models at two levels: either when initializing the backend for a default noise setting, or on a per-run basis for specific experiments.

**With ``PBackend``**

You can initialize a ``PBackend`` with a default noise model.

.. literalinclude:: /../tests/snippets/test_qiskit_backend_usage.py
   :language: python
   :start-after: # [backend_noise]
   :end-before: # [backend_noise]
   :dedent: 4

However, you can easily override this default by passing a different ``noise_model`` directly to the ``run`` method. This provides the flexibility to compare different noise scenarios without creating multiple backend instances.

.. literalinclude:: /../tests/test_backend.py
   :language: python
   :start-after: # [backend_override]
   :end-before: # [backend_override]
   :dedent: 4

**With ``PyrauliEstimator``**

The same principle applies to the ``PyrauliEstimator``. You can configure a default noise model during initialization or override it in the ``run`` call for specific Program-Backend-Unification (PUB) executions.

This example demonstrates how to set an initial ``NoiseModel`` on the estimator and then override it in a ``run`` call to apply a different noise channel for a specific job.

.. literalinclude:: /../tests/test_backend.py
   :language: python
   :start-after: # 2. Create an estimator with initial components
   :end-before: # 4. Assert the outcome
   :dedent: 4
