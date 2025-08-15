.. pyrauli documentation master file, created by
   sphinx-quickstart on Fri Aug 15 21:51:59 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pyrauli's documentation!
===================================

**pyrauli** is a high-performance Python package for quantum circuit simulation,
powered by the C++ `propauli`_ library. It uses Pauli back-propagation to
efficiently calculate the expectation values of observables.

This documentation provides tutorials, guides, and a complete API reference to
help you get the most out of the library.

.. _propauli: https://github.com/zeFresk/ProPauli

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   getting_started

.. toctree::
   :maxdepth: 2
   :caption: User Guides

   guides/observable_guide
   guides/circuit_guide
   guides/qiskit_integration_guide

.. toctree::
   :maxdepth: 2
   :caption: API Reference

   api

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
