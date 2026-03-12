"""
Conversion utilities between Qiskit and pyrauli objects.
"""

import logging
from qiskit.circuit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
import pyrauli
import math

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
        params = instruction.operation.params

        if op_name in ["h", "x", "y", "z"]:
            getattr(pyrauli_circuit, op_name)(qubits[0])
        elif op_name == "cx":
            pyrauli_circuit.add_operation("CX", qubits[0], qubits[1])
        elif op_name == "rz":
            pyrauli_circuit.add_operation("Rz", qubits[0], float(params[0]))
        elif op_name in ["u", "u3"]:
            theta, phi, lam = map(float, params)
            pyrauli_circuit.add_operation("u3", qubits[0], theta, phi, lam)
            
        # --- Decompositions ---
        elif op_name == "rx":
            # Decompose Rx(theta) -> H * Rz(theta) * H
            theta = float(params[0])
            target = qubits[0]
            
            pyrauli_circuit.h(target)
            pyrauli_circuit.rz(target, theta)
            pyrauli_circuit.h(target)
        elif op_name == "ry":
            # Decompose Ry(theta) -> Rz(-pi/2) * H * Rz(-theta) * H * Rz(pi/2)
            theta = float(params[0])
            target = qubits[0]
            
            # 1. Rz(pi/2)
            pyrauli_circuit.rz(target, math.pi / 2)
            # 2. H
            pyrauli_circuit.h(target)
            # 3. Rz(-theta)
            pyrauli_circuit.rz(target, -theta)
            # 4. H
            pyrauli_circuit.h(target)
            # 5. Rz(-pi/2)
            pyrauli_circuit.rz(target, -math.pi / 2)
        elif op_name == "cz":
            # Decompose CZ(c, t) -> H(t) CX(c, t) H(t)
            control, target = qubits[0], qubits[1]
            pyrauli_circuit.h(target)
            pyrauli_circuit.cx(control, target)
            pyrauli_circuit.h(target)
        elif op_name == "sx":
            # SQRT-X -> H * Rz(pi/2) * H
            target = qubits[0]
            pyrauli_circuit.h(target)
            pyrauli_circuit.rz(target, math.pi / 2)
            pyrauli_circuit.h(target)
        elif op_name == "sxdg": 
            # Inverse Sqrt-X -> H * Rz(-pi/2) * H
            target = qubits[0]
            pyrauli_circuit.h(target)
            pyrauli_circuit.rz(target, -math.pi / 2)
            pyrauli_circuit.h(target)
        elif op_name == "iswap":
            q0, q1 = qubits[0], qubits[1]
            
            # 1. Apply SWAP (Standard 3-CNOT decomposition)
            pyrauli_circuit.cx(q0, q1)
            pyrauli_circuit.cx(q1, q0)
            pyrauli_circuit.cx(q0, q1)
            
            # 2. Apply CZ -> H(1) CX(0,1) H(1)
            pyrauli_circuit.h(q1)
            pyrauli_circuit.cx(q0, q1)
            pyrauli_circuit.h(q1)
            
            # 3. Apply S gates (S = Rz(pi/2))
            pyrauli_circuit.rz(q0, math.pi / 2)
            pyrauli_circuit.rz(q1, math.pi / 2)
        elif op_name == "rzz":
            # Decompose Rzz(theta) -> CX(0,1) -> Rz(theta) on target -> CX(0,1)
            theta = float(params[0])
            q0, q1 = qubits[0], qubits[1]

            pyrauli_circuit.cx(q0, q1)
            pyrauli_circuit.rz(q1, theta)
            pyrauli_circuit.cx(q0, q1)

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
