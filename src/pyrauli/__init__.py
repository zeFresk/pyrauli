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
    LambdaTruncator,
    MultiTruncator,
    SchedulingPolicy,
    NeverPolicy,
    AlwaysBeforeSplittingPolicy,
    AlwaysAfterSplittingPolicy,
    Circuit,
    OperationType,
    Timing,
    SimulationState,
    CompressionResult,
    LambdaPolicy,
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
    "LambdaTruncator",
    "MultiTruncator",
    "SchedulingPolicy",
    "NeverPolicy",
    "AlwaysBeforeSplittingPolicy",
    "AlwaysAfterSplittingPolicy",
    "Circuit",
    "OperationType",
    "Timing",
    "SimulationState",
    "CompressionResult",
    "LambdaPolicy",
]

# Conditionally import Qiskit-related functionality
try:
    from . import backend
    from .backend import PBackend
    from . import converters
    from .converters import from_qiskit
    from . import estimator
    from .estimator import PyrauliEstimator

    __all__.extend(["backend", "PBackend", "converters", "from_qiskit"])
except ImportError:
    # This will fail if qiskit is not installed, which is expected.
    pass

from . import backend
from .backend import PBackend
from . import converters
from .converters import from_qiskit
from . import estimator
from .estimator import PyrauliEstimator

__all__.extend(["backend", "PBackend", "converters", "from_qiskit"])

