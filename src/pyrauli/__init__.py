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
    SymbolicCoefficient, SymbolicPauliTerm, SymbolicObservable, SymbolicNoise, SymbolicNoiseModel, SymbolicTruncator, SymbolicWeightTruncator, SymbolicNeverTruncator, SymbolicMultiTruncator, SymbolicCircuit
)

__all__ = [
    "PauliEnum", "PauliGate", "CliffordGate", "UnitalNoise", "QGate", "Pauli",
    "PauliTerm", "Observable", "Noise", "NoiseModel", "Truncator",
    "CoefficientTruncator", "WeightTruncator", "KeepNTruncator", "NeverTruncator",
    "LambdaTruncator", "MultiTruncator", "SchedulingPolicy", "NeverPolicy",
    "AlwaysBeforeSplittingPolicy", "AlwaysAfterSplittingPolicy", "Circuit",
    "OperationType", "Timing", "SimulationState", "CompressionResult",
    "LambdaPolicy",
    "SymbolicCoefficient", "SymbolicObservable", "SymbolicPauliTerm", "SymbolicNoise", "SymbolicNoiseModel", "SymbolicTruncator", "SymbolicWeightTruncator", "SymbolicNeverTruncator", "SymbolicMultiTruncator", "SymbolicCircuit"

]

try:
    import sympy
    def to_sympy(self):
        """
        Converts the SymbolicCoefficient to a SymPy expression.

        Returns:
            A SymPy expression equivalent to the SymbolicCoefficient.
        """
        return sympy.sympify(self.to_string())
    SymbolicCoefficient.to_sympy = to_sympy
except ImportError:
    pass

# Conditionally import Qiskit-related functionality
try:
    from .backend import PBackend
    from .converters import from_qiskit
    from .estimator import PyrauliEstimator

    __all__.extend(["PBackend", "from_qiskit", "PyrauliEstimator"])
except ImportError:
    # This will fail if qiskit is not installed, which is expected.
    pass
