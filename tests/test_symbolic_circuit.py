from pyrauli import (
    SymbolicCircuit,
    SymbolicObservable,
    SymbolicNoiseModel,
    SymbolicWeightTruncator,
    UnitalNoise,
    SymbolicCoefficient,
    QGate
)
import math
import pytest


def test_init():
    SymbolicCircuit(2)
    SymbolicCircuit(2, truncator=SymbolicWeightTruncator(1))


def test_add_operations():
    circuit = SymbolicCircuit(2)
    circuit.add_operation("H", 0)
    circuit.add_operation("CX", 0, 1)
    circuit.add_operation("Rz", 1, "theta")


def test_run_symbolic():
    circuit = SymbolicCircuit(1)
    circuit.add_operation("H", 0)
    circuit.add_operation("Rz", 0, "theta")
    circuit.add_operation("H", 0)

    obs = SymbolicObservable("Z")
    final_obs = circuit.run(obs)

    assert final_obs.expectation_value().evaluate({"theta": 0}) == pytest.approx(1.0)
    assert final_obs.expectation_value().evaluate({"theta": 3.14159}) == pytest.approx(
        -1.0
    )


def test_with_noise():
    noise = SymbolicNoiseModel()
    noise.add_unital_noise_on_gate(QGate.H, UnitalNoise.Depolarizing, "p")

    circuit = SymbolicCircuit(1, noise_model=noise)
    circuit.add_operation("H", 0)

    obs = SymbolicObservable("X")
    final_obs = circuit.run(obs)

    # With no noise, H|X> = |Z>, EV = 1
    assert final_obs.expectation_value().evaluate({"p": 0}) == pytest.approx(1.0)
    # With full depolarizing, state is mixed, EV = 0
    assert final_obs.expectation_value().evaluate({"p": 1.0}) == pytest.approx(0.0)


def test_reset():
    circuit = SymbolicCircuit(1)
    circuit.add_operation("H", 0)
    circuit.reset()
    obs = SymbolicObservable("Z")
    final_obs = circuit.run(obs)
    assert final_obs[0] == obs[0]

def test_run_symbolic_u3():
    """
    Tests the symbolic evaluation of a U3 gate parameterized with strings.
    """
    circuit = SymbolicCircuit(1)
    theta = SymbolicCoefficient("theta")
    phi = SymbolicCoefficient("phi")
    lbd = SymbolicCoefficient("lambda")
    
    # Apply a U3 gate entirely using symbolic variables
    circuit.add_operation("u3", 0, theta, phi, lbd)

    obs = SymbolicObservable("Z")
    final_obs = circuit.run(obs)

    # Evaluate at theta = 0 (Expectation value of Z = cos(0) = 1.0)
    # phi and lambda don't affect the Z expectation value from |0>
    ev_zero = final_obs.expectation_value().evaluate({
        "theta": 0.0, 
        "phi": 1.0, 
        "lambda": 2.0
    })
    assert ev_zero == pytest.approx(1.0)

    # Evaluate at theta = pi (Expectation value of Z = cos(pi) = -1.0)
    ev_pi = final_obs.expectation_value().evaluate({
        "theta": math.pi, 
        "phi": 0.0, 
        "lambda": 0.0
    })
    assert ev_pi == pytest.approx(-1.0)
    
    # Evaluate at theta = pi/2 (Expectation value of Z = cos(pi/2) = 0.0)
    ev_half_pi = final_obs.expectation_value().evaluate({
        "theta": math.pi / 2.0, 
        "phi": math.pi, 
        "lambda": math.pi
    })
    assert ev_half_pi == pytest.approx(0.0, abs=1e-7)
