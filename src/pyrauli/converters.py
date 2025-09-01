"""
Conversion utilities between Qiskit and pyrauli objects.
"""

import logging
from qiskit.circuit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
import pyrauli

def from_qiskit(qiskit_obj, noise_model: pyrauli.NoiseModel = None, reverse=False):
    """
    Converts a Qiskit object to its pyrauli equivalent.

    Args:
        qiskit_obj: The Qiskit object to convert (QuantumCircuit or SparsePauliOp).
        noise_model: A pyrauli NoiseModel to apply to the circuit.

    Returns:
        The equivalent pyrauli object.
    """
    if isinstance(qiskit_obj, QuantumCircuit):
        return from_qiskit_qc(qiskit_obj, noise_model=noise_model)
    elif isinstance(qiskit_obj, SparsePauliOp):
        return from_qiskit_obs(qiskit_obj, reverse=reverse)
    else:
        raise ValueError(f"Can't convert object of type {type(qiskit_obj)} to pyrauli object.")

def from_qiskit_qc(qiskit_circuit: QuantumCircuit, noise_model: pyrauli.NoiseModel = None) -> pyrauli.Circuit:
    """
    Translates a Qiskit QuantumCircuit into a pyrauli.Circuit.
    """
    num_qubits = qiskit_circuit.num_qubits
    nm = noise_model if noise_model is not None else pyrauli.NoiseModel()
    pyrauli_circuit = pyrauli.Circuit(num_qubits, noise_model=nm)

    for instruction in qiskit_circuit.data:
        op_name = instruction.operation.name.lower()
        qubits = [qiskit_circuit.find_bit(q).index for q in instruction.qubits]

        if op_name == "h":
            pyrauli_circuit.add_operation("H", qubits[0])
        elif op_name == "cx":
            pyrauli_circuit.add_operation("CX", qubits[0], qubits[1])
        elif op_name == "rz":
            theta = instruction.operation.params[0]
            pyrauli_circuit.add_operation("Rz", qubits[0], float(theta))
        elif op_name not in ["measure", "barrier"]:
            raise NotImplementedError(
                f"Gate '{op_name}' is not supported by the converter."
            )

    return pyrauli_circuit

def from_qiskit_obs(qiskit_obs: SparsePauliOp, reverse=False) -> pyrauli.Observable:
    """
    Translates a Qiskit SparsePauliOp to a pyrauli.Observable.
    """
    pts = []
    for pauli_string, coeff in zip(qiskit_obs.paulis, qiskit_obs.coeffs):
        if coeff.imag != 0.:
            logging.warning("pyrauli observables don't support complex coefficients.")

        ps = pauli_string.to_label()
        if reverse:
            ps = ps[::-1]

        pt = pyrauli.PauliTerm(ps, float(coeff.real))
        pts.append(pt)
    return pyrauli.Observable(pts)
