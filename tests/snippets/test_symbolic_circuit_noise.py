from pyrauli import SymbolicCircuit, SymbolicObservable, SymbolicNoiseModel, UnitalNoise, QGate
import pytest

def test_symbolic_noise():
    # [symbolic_noise]
    # 1. Define a symbolic noise model
    noise_model = SymbolicNoiseModel()
    noise_model.add_unital_noise_on_gate(QGate.H, UnitalNoise.Depolarizing, "p_noise")

    # 2. Create a circuit with the noise model
    circuit = SymbolicCircuit(1, noise_model=noise_model)
    circuit.add_operation("H", 0)

    # 3. Run the simulation
    observable = SymbolicObservable("X")
    final_observable = circuit.run(observable)
    result = final_observable.expectation_value()

    # 4. Evaluate for different noise levels
    print(f"Expectation value with no noise: {result.evaluate({'p_noise': 0.0})}")
    print(f"Expectation value with some noise: {result.evaluate({'p_noise': 0.1})}")
    # [symbolic_noise]
