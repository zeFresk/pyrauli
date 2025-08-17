import pytest
from pyrauli import Circuit, Observable, NoiseModel, QGate, UnitalNoise


def test_noise_model_application():
    """
    Tests that a noise model correctly alters the simulation result.
    """
    # [noisy_circuit]
    # 1. Create a Noise Model that adds depolarizing noise after every H gate and amplitude damping noise after each X gate
    p = 0.1  # Noise strength
    noise_model = NoiseModel()
    noise_model.add_unital_noise_on_gate(QGate.H, UnitalNoise.Depolarizing, p)
    noise_model.add_amplitude_damping_on_gate(QGate.X, p)

    # 2. Create a noisy circuit using the noise model
    qc_noisy = Circuit(1, noise_model=noise_model)
    qc_noisy.add_operation("H", 0)

    # 3. Run, everything is taken care of automatically
    res_noisy = qc_noisy.run(Observable("X"))
    # [noisy_circuit]

    # 2. Create a noiseless reference circuit
    qc_noiseless = Circuit(1)
    qc_noiseless.add_operation("H", 0)

    # 4. Define an observable.
    # For H applied to X, the final observable is Z. Expval = <0|Z|0> = 1.
    obs = Observable("X")

    # 5. Run both simulations
    res_noiseless = qc_noiseless.run(obs)

    # 6. Assert results
    # The depolarizing channel P(O) = (1-p)O. So the final expectation
    # value should be scaled by (1-p).
    assert res_noiseless.expectation_value() == pytest.approx(1.0)
    assert res_noisy.expectation_value() == pytest.approx(1.0 - p)
