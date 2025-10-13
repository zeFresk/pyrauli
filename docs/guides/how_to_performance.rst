.. _how_to_performance:

Optimize Performance with Parallel Execution
============================================

``pyrauli`` is designed for high-performance simulation, and its C++ backend
includes a parallel execution engine powered by OpenMP. This guide shows how
to leverage this feature to significantly speed up simulations, especially
when working with many observables.

The `RuntimePolicy`
-------------------

The execution strategy is controlled by a :py:class:`~pyrauli.RuntimePolicy` object.
``pyrauli`` provides two policies:

* ``pyrauli.seq``: A sequential (single-threaded) execution policy.
* ``pyrauli.par``: A parallel (multi-threaded) execution policy.

You can pass these policies to the ``runtime`` parameter of the simulation methods.

Running a Single Observable in Parallel
---------------------------------------

You can achieve a performance boost even when simulating just a single observable
by using the parallel runtime. The internal operations for evolving the observable—especially
during splitting gates like Rz—are parallelized across multiple CPU cores.

While this is faster than sequential execution, it is not as efficient as parallel
batching. The overhead of managing threads is better amortized when distributed
across many independent observables.

.. literalinclude:: /../tests/snippets/test_performance_guide.py
   :language: python
   :start-after: # [single_parallel]
   :end-before: # [single_parallel]
   :dedent: 4

Batching Observables for Maximum Throughput
-------------------------------------------

The greatest performance benefit of the parallel engine comes from batching—that is,
running the circuit simulation for a *list* of observables in a single call.
``pyrauli`` will automatically distribute the work across multiple CPU cores.

The example below computes the expectation values for three different observables
in one parallel call.

.. literalinclude:: /../tests/snippets/test_performance_guide.py
   :language: python
   :start-after: # [batch_observables]
   :end-before: # [batch_observables]
   :dedent: 4

.. TIP::
    Always prefer passing a list of observables to a single ``.expectation_value()``
    or ``.run()`` call over looping in Python. The performance gain from
    processing the batch in C++ is substantial.

Enabling Parallelism in Qiskit
-------------------------------

When using ``pyrauli`` with Qiskit, you can enable parallel execution by default
by passing the policy during the backend or estimator's initialization.

.. literalinclude:: /../tests/snippets/test_performance_guide.py
   :language: python
   :start-after: # [qiskit_parallel]
   :end-before: # [qiskit_parallel]
   :dedent: 4
