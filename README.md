# pyrauli: A Python Wrapper for ProPauli

[![Build and test package](https://github.com/zeFresk/pyrauli/actions/workflows/ci.yml/badge.svg)](https://github.com/zeFresk/pyrauli/actions/workflows/ci.yml)
[![Documentation](https://img.shields.io/badge/Documentation-View-blue)](https://zefresk.github.io/pyrauli/)
[![Coverage Status](https://coveralls.io/repos/github/zeFresk/pyrauli/badge.svg?branch=coverage)](https://coveralls.io/github/zeFresk/pyrauli?branch=coverage)
[![Latest benchmarks](https://img.shields.io/badge/Benchmarks-View-blue)](https://zefresk.github.io/pyrauli/dev/bench)

**pyrauli** is a high-performance Python package for quantum circuit simulation, powered by the C++ `propauli` library. It uses Pauli back-propagation to efficiently calculate the expectation values of observables.

This package provides a clean Pythonic interface to the core C++ engine and includes an optional, fully-featured backend for **Qiskit**, allowing it to be used as a simulator within the Qiskit ecosystem.

## Features

- **High-Performance Core**: Leverages the speed of C++ for simulation.
- **Pauli Propagation**: Evolve observables backward through the circuit for efficient expectation value calculation.
- **Optional Qiskit Integration**: Install with `[qiskit]` to get a `BackendV2`-compliant simulator.
- **Modern & Easy to Install**: Built with `scikit-build-core` and CMake's `FetchContent` for a seamless `pip install` experience.

## Installation

You can install `pyrauli` directly from PyPI (once published) or from the source.

**Standard Installation:**
```bash
pip install pyrauli
```

NOTE: Python >= 3.9 required.

**Installation with Qiskit Support:**

```bash
pip install 'pyrauli[qiskit]'
```

## Quick Start

### Core Usage

```python
import pyrauli
import math

# Create a 2-qubit circuit
qc = pyrauli.Circuit(2)

# Add gates
qc.add_operation("H", 0)
qc.add_operation("CX", 0, 1)

# Define an observable and run the circuit
observable = pyrauli.Observable("ZI")
final_observable = qc.run(observable)

print(f"Expectation value of ZI: {final_observable.expectation_value()}")
```

### Qiskit Backend Usage

```python
from qiskit.circuit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from pyrauli import PBackend

# Create a Qiskit circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

# Define an observable and instantiate the backend
obs = SparsePauliOp("ZI")
backend = PBackend()

# Run using the PUB (Primitive Unified Bloc) format
job = backend.run([(qc, obs)])
result = job.result()
ev = result.results[0].data.evs[0]

print(f"Expectation value from Qiskit backend: {ev}")
```
