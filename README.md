# pyrauli: High-Performance Quantum Circuit Simulation

[![Build and test package](https://github.com/zeFresk/pyrauli/actions/workflows/ci.yml/badge.svg)](https://github.com/zeFresk/pyrauli/actions/workflows/ci.yml)
[![Documentation](https://img.shields.io/badge/Documentation-View-blue)](https://zefresk.github.io/pyrauli/)
[![Coverage Status](https://coveralls.io/repos/github/zeFresk/pyrauli/badge.svg?branch=coverage)](https://coveralls.io/github/zeFresk/pyrauli?branch=coverage)
[![Latest benchmarks](https://img.shields.io/badge/Benchmarks-View-blue)](https://zefresk.github.io/pyrauli/dev/bench)

**pyrauli** is a high-performance Python package for quantum circuit simulation, powered by the [C++ `ProPauli` library](https://github.com/zeFresk/ProPauli/). It leverages the Heisenberg picture and a technique called Pauli back-propagation to efficiently calculate the expectation values of observables, making it particularly well-suited for certain classes of variational quantum algorithms and noise analysis.

## Key Features

*   **High-Performance C++ Backend**: Core simulation logic is implemented in C++ with **OpenMP parallel execution support** for maximum speed.
*   **Efficient Heisenberg Picture Simulation**: Observables are evolved instead of the state vector, offering significant advantages for calculating expectation values on large systems.
*   **Direct Hamiltonian Evolution**: Simulate time evolution `exp(-iHt)` for complex, multi-local Hamiltonians with a single optimized operation.
*   **Native Batch Processing**: Simulate lists of observables in a single, parallelized call for massive throughput.
*   **Seamless Qiskit Integration**: Use `pyrauli` as a drop-in backend or via the `PyrauliEstimator` primitive for modern, algorithm-focused development.
*   **Advanced Complexity Management**: Fine-grained control over the simulation via customizable `Truncator` and `SchedulingPolicy` objects, with **built-in truncation error tracking**.
*   **Powerful Symbolic Toolkit**: Simulate parameterized circuits with symbolic gate angles, noise strengths, and truncation thresholds.

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

**Installation with Parallel Support**

To enable high-performance parallel execution engine, install alongside an existing OpenMP compiler.
Most user should not have to do anything to enable parallelism.

```bash
pip install pyrauli 
```

Note for macOS users: The parallel engine requires the OpenMP runtime. You may need to install it separately, e.g., via Homebrew: `brew install libomp`.

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
expectation_value = final_observable.expectation_value()

print(f"Final observable: {final_observable}")
print(f"Expectation value: {expectation_value}")
print(f"Truncation error: {final_observable.truncate_error()}") # 0 here

# Expected output:
# Final observable: +1 XI
# Expectation value: 0.0
# Truncation error: 0.0
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
 
## Advanced Usage: Direct Hamiltonian Evolution

`pyrauli` excels at simulating time evolution under complex, non-local Hamiltonians. The `eiht` method allows you to apply the operation `exp(-iHt)` in a single step, where `H` is a multi-qubit Pauli string. This is significantly more efficient and expressive than decomposing the operation into standard gates.

The following example simulates an 8-qubit system evolving under a 4-local Wen Plaquette operator, `H = X_0 Z_1 X_4 Z_5`.

```python
import pyrauli
import math

# 1. Define simulation parameters
n_qubits = 8
time = 0.5

# 2. Define the Hamiltonian axis as a list of Pauli strings
# This corresponds to the operator H = X_0 Z_1 X_4 Z_5
hamiltonian_axis = ["X", "Z", "I", "I", "X", "Z", "I", "I"]

# 3. Build the circuit
circuit = pyrauli.Circuit(n_qubits)

# Apply the Hamiltonian evolution in a single, efficient operation
circuit.eiht(hamiltonian_axis, time)

# 4. Define an observable to measure
observable = pyrauli.Observable("ZIIIIIII") # Z on qubit 0

# 5. Run the simulation
ev, err = circuit.expectation_value(observable)

print(f"Expectation value of Z_0 after evolution: {ev:.4f}")
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
