import pyrauli
import math

def test_basic_circuit_snippet():
    # [basic_circuit]
    # Create a 2-qubit circuit
    qc = pyrauli.Circuit(2)

    # Add gates
    qc.add_operation("H", 0)
    qc.add_operation("CX", 0, 1)

    # Define an observable and run the circuit
    observable = pyrauli.Observable("ZI")
    final_observable = qc.run(observable)

    print(f"Expectation value of ZI: {final_observable.expectation_value()}")
    # [basic_circuit]
