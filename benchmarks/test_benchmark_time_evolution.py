import pyrauli
import pytest

def build_wen_plaquette_circuit(t=0.5):
    """
    Builds an 8-qubit circuit for time evolution under a Wen Plaquette operator.
    The Hamiltonian is H = X_0 Z_1 X_4 Z_5.
    """
    n_qubits = 8
    
    # The Hamiltonian axis corresponds to H = X_0 Z_1 X_4 Z_5
    hamiltonian_axis = ["X", "Z", "I", "I", "X", "Z", "I", "I"]
    
    circuit = pyrauli.Circuit(n_qubits)
    circuit.eiht(hamiltonian_axis, t)
    
    return circuit

def test_wen_plaquette_benchmark(benchmark):
    """
    Benchmark for an 8-qubit Hamiltonian time evolution using the eiht gate.
    """
    # 1. Setup the circuit and observable
    evolution_time = 0.5
    circuit = build_wen_plaquette_circuit(t=evolution_time)
    observable = pyrauli.Observable("ZIIIIIII") # Measure Z_0

    # 2. Define the function to be benchmarked
    def run_simulation():
        circuit.expectation_value(observable, runtime=pyrauli.seq)

    # 3. Run the benchmark
    benchmark(run_simulation)
