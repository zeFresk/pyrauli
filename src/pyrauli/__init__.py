# src/pyrauli/__init__.py
from ._core import (
    PauliEnum,
    PauliGate,
    CliffordGate,
    UnitalNoise,
    QGate,
    Pauli,
    PauliTerm,
    Observable,
    Noise,
    NoiseModel,
    Truncator,
    CoefficientTruncator,
    WeightTruncator,
    NeverTruncator,
    SchedulingPolicy,
    NeverPolicy,
    AlwaysBeforeSplittingPolicy,
    AlwaysAfterSplittingPolicy,
    Circuit,
)

__all__ = [
    "PauliEnum",
    "PauliGate",
    "CliffordGate",
    "UnitalNoise",
    "QGate",
    "Pauli",
    "PauliTerm",
    "Observable",
    "Noise",
    "NoiseModel",
    "Truncator",
    "CoefficientTruncator",
    "WeightTruncator",
    "NeverTruncator",
    "SchedulingPolicy",
    "NeverPolicy",
    "AlwaysBeforeSplittingPolicy",
    "AlwaysAfterSplittingPolicy",
    "Circuit",
]

# Conditionally import Qiskit-related functionality
try:
    from . import backend
    from .backend import PBackend
    from . import converters
    from .converters import from_qiskit

    __all__.extend(["backend", "PBackend", "converters", "from_qiskit"])
except ImportError:
    # This will fail if qiskit is not installed, which is expected.
    pass
