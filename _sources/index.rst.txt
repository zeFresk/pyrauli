.. pyrauli documentation master file, created by
   sphinx-quickstart on Fri Aug 15 21:51:59 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pyrauli's documentation!
===================================

**pyrauli** is a high-performance Python package for quantum circuit simulation,
powered by the C++ `ProPauli`_ library.
It uses Pauli back-propagation to
efficiently calculate the expectation values of observables.

This documentation is structured to help you succeed, whether you are learning
the library for the first time or need a specific technical detail.

.. _ProPauli: https://github.com/zeFresk/ProPauli

.. toctree::
   :maxdepth: 2
   :caption: Tutorials

   tutorials/getting_started

.. toctree::
   :maxdepth: 2
   :caption: How-To Guides

   guides/how_to_circuit
   guides/how_to_observables
   guides/how_to_complexity
   guides/how_to_qiskit
   guides/how_to_noise

.. toctree::
   :maxdepth: 2
   :caption: Explanation

   explanation/theory

.. toctree::
   :maxdepth: 2
   :caption: API Reference

   reference/api

.. toctree::
   :maxdepth: 2 
   :caption: Performance 

   Benchmarks <https://zefresk.github.io/pyrauli/dev/bench/>

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
