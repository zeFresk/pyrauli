from pyrauli import Observable, CliffordGate

def test_observable_manual_evolution_snippet():
    # [observable_manual_evolution]
    # Start with a simple Z observable on the first of two qubits
    obs = Observable("ZI")
    print(f"Initial observable: {obs}")

    # Evolve the observable backward through a CNOT gate
    # Note: control and target are for the forward circuit, but applied in reverse
    obs.apply_cx(0, 1)
    print(f"After CX(0,1):      {obs}")

    # Evolve backward through an H gate on qubit 0
    obs.apply_clifford(CliffordGate.H, 0)
    print(f"After H(0):         {obs}")
    # [observable_manual_evolution]

    # Add an assertion to make it a valid test
    assert str(obs) == "+1 XI"
