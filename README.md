# pyrauli: High-Performance Quantum Circuit Simulation

[![Build and test package](https://github.com/zeFresk/pyrauli/actions/workflows/ci.yml/badge.svg)](https://github.com/zeFresk/pyrauli/actions/workflows/ci.yml)
[![Documentation](https://img.shields.io/badge/Documentation-View-blue)](https://zefresk.github.io/pyrauli/)
[![Coverage Status](https://coveralls.io/repos/github/zeFresk/pyrauli/badge.svg?branch=coverage)](https://coveralls.io/github/zeFresk/pyrauli?branch=coverage)
[![Latest benchmarks](https://img.shields.io/badge/Benchmarks-View-blue)](https://zefresk.github.io/pyrauli/dev/bench)

**pyrauli** is a high-performance Python package for quantum circuit simulation, powered by the [C++ `ProPauli` library](https://github.com/zeFresk/ProPauli/). It leverages the Heisenberg picture and a technique called Pauli back-propagation to efficiently calculate the expectation values of observables, making it particularly well-suited for certain classes of variational quantum algorithms and noise analysis.

## Key Features

  * **High Performance**: Core simulation logic is implemented in C++ for maximum speed, wrapped in a user-friendly Python API.
  * **Heisenberg Picture Simulation**: Observables are evolved instead of the state vector, which can be significantly more efficient for calculating expectation values on large quantum systems.
  * **Seamless Qiskit Integration**: Use `pyrauli` as a drop-in backend for your existing Qiskit workflows, or leverage the `PyrauliEstimator` primitive for modern, algorithm-focused development.
  * **Advanced Complexity Management**: Fine-grained control over the simulation's resource usage through customizable `Truncator` and `SchedulingPolicy` objects.

## Installation

`pyrauli` requires Python 3.9 or later. It can be installed from PyPI using pip.

**Standard Installation**

For core functionality:

```bash
pip install pyrauli
````

**Installation with Qiskit Support**

To enable the Qiskit integration features, install the `[qiskit]` extra:

```bash
pip install 'pyrauli[qiskit]'
````

## Quick Start

Simulate a simple 2-qubit Bell state circuit and calculate the expectation value of the $Z \\otimes I$ observable.

```python
import pyrauli

# 1. Initialize a 2-qubit circuit
circuit = pyrauli.Circuit(2)

# 2. Add quantum operations
circuit.add_operation("H", 0)      # Hadamard on qubit 0
circuit.add_operation("CX", 0, 1)  # CNOT with control 0, target 1

# 3. Define an observable
# Here, we measure the Pauli Z observable on qubit 0
observable = pyrauli.Observable("ZI")

# 4. Run the simulation
# This evolves the observable backward through the circuit
final_observable = circuit.run(observable)

# 5. Retrieve the final expectation value
# The expectation value is calculated with respect to the initial |00...0> state
expectation_value = final_observable.get_expectation_value()

print(f"Final observable: {final_observable}")
print(f"Expectation value: {expectation_value}")

# Expected output:
# Final observable: +1 XI
# Expectation value: 0.0
```

## Qiskit Backend Usage

```python
from qiskit.circuit import QuantumCircuit, Parameter
from qiskit.transpiler import generate_preset_pass_manager
from qiskit.quantum_info import SparsePauliOp
from pyrauli import PBackend

# Create a parameterized Qiskit circuit
theta = Parameter('theta')
qc = QuantumCircuit(2)
qc.h(0)
qc.rz(theta, 0)
qc.cx(0, 1)

# Define an observable and instantiate the backend
obs = SparsePauliOp("ZI")
backend = PBackend()

# transpilation is supported (but not needed here)
pm = generate_preset_pass_manager(backend)
isa_qc = pm.run(qc)

# Run using the PUB (Primitive Unified Bloc) format
job = backend.run([(qc, obs, [3.14])])
result = job.result()
ev = result[0].data.evs[0]

print(f"Expectation value: {ev}")
```

## Documentation

For comprehensive information, including tutorials, how-to guides, and the full API reference, please visit the official documentation:
**https://zefresk.github.io/pyrauli/**

## benchmarks

**pyrauli** latest benchmarks results are available here: **https://zefresk.github.io/pyrauli/dev/bench/**

## References

This work is based on and implements ideas from the following articles:

  * _Pauli Propagation: A Computational Framework for Simulating Quantum Systems_, by Manuel S. Rudolph, Tyson Jones, Yanting Teng, Armando Angrisani, Zoë Holmes [https://arxiv.org/abs/2505.21606](https://arxiv.org/abs/2505.21606)

  * _Efficient simulation of parametrized quantum circuits under non-unital noise through Pauli backpropagation_, by Victor Martinez, Armando Angrisani, Ekaterina Pankovets, Omar Fawzi, Daniel Stilck França [https://arxiv.org/abs/2501.13050](https://arxiv.org/abs/2501.13050)
