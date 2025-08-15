import pytest
from pyrauli import Circuit, Observable, NoiseModel, QGate, UnitalNoise


def test_noise_model_application():
    """
    Tests that a noise model correctly alters the simulation result.
    """
    # 1. Create a Noise Model that adds depolarizing noise after every H gate
    p = 0.1  # Noise probability
    noise_model = NoiseModel()
    noise_model.add_unital_noise_on_gate(QGate.H, UnitalNoise.Depolarizing, p)

    # 2. Create a noiseless reference circuit
    qc_noiseless = Circuit(1)
    qc_noiseless.add_operation("H", 0)

    # 3. Create a noisy circuit using the noise model
    qc_noisy = Circuit(1, noise_model=noise_model)
    qc_noisy.add_operation("H", 0)

    # 4. Define an observable.
    # For H applied to X, the final observable is Z. Expval = <0|Z|0> = 1.
    obs = Observable("X")

    # 5. Run both simulations
    res_noiseless = qc_noiseless.run(obs)
    res_noisy = qc_noisy.run(obs)

    # 6. Assert results
    # The depolarizing channel P(O) = (1-p)O. So the final expectation
    # value should be scaled by (1-p).
    assert res_noiseless.expectation_value() == pytest.approx(1.0)
    assert res_noisy.expectation_value() == pytest.approx(1.0 - p)
