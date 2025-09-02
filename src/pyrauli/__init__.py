"""
pyrauli: A Python Wrapper for ProPauli

This package provides a high-performance Python interface for quantum circuit
simulation, powered by the C++ `propauli` library.
"""

from ._core import (
    PauliEnum, PauliGate, CliffordGate, UnitalNoise, QGate, Pauli, PauliTerm,
    Observable, Noise, NoiseModel, Truncator, CoefficientTruncator,
    WeightTruncator, KeepNTruncator, NeverTruncator, LambdaTruncator, MultiTruncator,
    SchedulingPolicy, NeverPolicy, AlwaysBeforeSplittingPolicy,
    AlwaysAfterSplittingPolicy, Circuit, OperationType, Timing,
    SimulationState, CompressionResult, LambdaPolicy,
)

__all__ = [
    "PauliEnum", "PauliGate", "CliffordGate", "UnitalNoise", "QGate", "Pauli",
    "PauliTerm", "Observable", "Noise", "NoiseModel", "Truncator",
    "CoefficientTruncator", "WeightTruncator", "KeepNTruncator", "NeverTruncator",
    "LambdaTruncator", "MultiTruncator", "SchedulingPolicy", "NeverPolicy",
    "AlwaysBeforeSplittingPolicy", "AlwaysAfterSplittingPolicy", "Circuit",
    "OperationType", "Timing", "SimulationState", "CompressionResult",
    "LambdaPolicy",
]

# Conditionally import Qiskit-related functionality
try:
    from .backend import PBackend
    from .converters import from_qiskit
    from .estimator import PyrauliEstimator

    __all__.extend(["PBackend", "from_qiskit", "PyrauliEstimator"])
except ImportError:
    # This will fail if qiskit is not installed, which is expected.
    pass
