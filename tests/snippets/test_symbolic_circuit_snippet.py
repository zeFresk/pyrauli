from pyrauli import SymbolicCircuit, SymbolicObservable

def test_symbolic_obs():
    # [symbolic_circuit]
    circuit = SymbolicCircuit(1)
    circuit.add_operation("H", 0)
    circuit.add_operation("Rz", 0, "theta")
    circuit.add_operation("H", 0)
    # [symbolic_circuit]

    observable = SymbolicObservable("Z")

    # [symbolic_evaluation]
    final_observable = circuit.run(observable)
    expectation_value = final_observable.expectation_value()

    # Call this before evaluating
    compiled_ev = expectation_value.compile()

    # Recommanded for printing
    simplified_ev = expectation_value.simplified()

    # Evaluate for a specific angle
    value = compiled_ev.evaluate({"theta": 3.14159 / 4})
    # [symbolic_evaluation]
