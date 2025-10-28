import pyrauli
import math
import pytest

def test_eiht_basic_usage():
    # [eiht_basic_usage]
    n_qubits = 8
    evolution_time = 0.5

    # Define the Hamiltonian axis for H = X_0 Z_1 X_4 Z_5
    hamiltonian_axis = ["X", "Z", "I", "I", "X", "Z", "I", "I"]

    # 1. Build the circuit
    circuit = pyrauli.Circuit(n_qubits)
    circuit.eiht(hamiltonian_axis, evolution_time)

    # 2. Define an observable to measure
    observable = pyrauli.Observable("ZIIIIIII") # Z on qubit 0

    # 3. Run the simulation and get the result
    ev, err = circuit.expectation_value(observable)

    print(f"Expectation value of Z_0 at t={evolution_time}: {ev:.4f}")
    
    # Verify the result (for this case, EV = cos(2*t))
    expected = math.cos(2 * evolution_time)
    print(f"Expected theoretical value: {expected:.4f}")
    # [eiht_basic_usage]
    assert ev == pytest.approx(expected)


def test_rp_vs_eiht():
    # [rp_vs_eiht]
    n_qubits = 4
    time = 0.25
    axis = ["X", "Y", "Z", "I"]

    # Create one circuit using eiht
    circuit_eiht = pyrauli.Circuit(n_qubits)
    circuit_eiht.eiht(axis, time)

    # Create another circuit using rp with theta = 2*t
    circuit_rp = pyrauli.Circuit(n_qubits)
    circuit_rp.rp(axis, 2 * time)

    # They should produce the exact same result
    observable = pyrauli.Observable("ZIII")
    ev_eiht, _ = circuit_eiht.expectation_value(observable)
    ev_rp, _ = circuit_rp.expectation_value(observable)

    print(f"Result from eiht(t={time}): {ev_eiht:.4f}")
    print(f"Result from rp(theta={2*time}):   {ev_rp:.4f}")
    assert ev_eiht == pytest.approx(ev_rp)
    # [rp_vs_eiht]


def test_symbolic_evolution():
    # [symbolic_evolution]
    n_qubits = 4
    axis = ["X", "Y", "Z", "I"]

    # 1. Build a SymbolicCircuit with a variable 't' for time
    symbolic_circuit = pyrauli.SymbolicCircuit(n_qubits)
    symbolic_circuit.eiht(axis, pyrauli.SymbolicCoefficient("t"))

    # 2. Run the simulation on a standard observable
    observable = pyrauli.SymbolicObservable("ZIII")
    final_observable = symbolic_circuit.run(observable)

    # 3. The final expectation value is a symbolic expression of 't'
    symbolic_ev = final_observable.expectation_value()
    print(f"Symbolic expectation value: {symbolic_ev}")

    # 4. Evaluate the expression for different concrete times
    times_to_check = [0.0, 0.5, 1.0]
    for t_val in times_to_check:
        numeric_ev = symbolic_ev.evaluate({"t": t_val})
        print(f"EV at t={t_val}: {numeric_ev:.4f}")
    # [symbolic_evolution]
    assert "t" in symbolic_ev.to_string()
