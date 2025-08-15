import logging
from qiskit.circuit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
import pyrauli


def from_qiskit(qiskit_obj: type[QuantumCircuit | SparsePauliOp], noise_model : pyrauli.NoiseModel = None):
    if isinstance(qiskit_obj, QuantumCircuit):
        return from_qiskit_qc(qiskit_obj, noise_model=noise_model)
    elif isinstance(qiskit_obj, SparsePauliOp):
        return from_qiskit_obs(qiskit_obj)
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


def from_qiskit_obs(qiskit_obs: SparsePauliOp):
    """
    Translates a Qiskit observable to pyrauli observable
    """
    pts = []
    for pauli_string, coeff in zip(qiskit_obs.paulis, qiskit_obs.coeffs):
        if coeff.imag != 0.:
            logging.warning("pyrauli observables doesn't support complex coefficient values for observables.")
        pt = pyrauli.PauliTerm(pauli_string.to_label(), float(coeff.real))
        pts += [pt]
    pyrauli_obs = pyrauli.Observable(pts)
    print(pyrauli_obs)
    return pyrauli_obs
