from qiskit.circuit import QuantumCircuit
import pyrauli

def from_qiskit(qiskit_circuit: QuantumCircuit) -> pyrauli.Circuit:
    """
    Translates a Qiskit QuantumCircuit into a pyrauli.Circuit.
    """
    num_qubits = qiskit_circuit.num_qubits
    pyrauli_circuit = pyrauli.Circuit(num_qubits)

    for instruction in qiskit_circuit.data:
        op_name = instruction.operation.name.lower()

        # --- THIS IS THE FIX ---
        # Use the modern `find_bit(qubit).index` method to get the integer index
        # of each qubit involved in the instruction.
        qubits = [qiskit_circuit.find_bit(q).index for q in instruction.qubits]

        if op_name == "h":
            pyrauli_circuit.add_operation("H", qubits[0])
        elif op_name == "cx":
            pyrauli_circuit.add_operation("CX", qubits[0], qubits[1])
        elif op_name == "rz":
            theta = instruction.operation.params[0]
            pyrauli_circuit.add_operation("Rz", qubits[0], float(theta))
        elif op_name not in ["measure", "barrier"]:
            raise NotImplementedError(f"Gate '{op_name}' is not supported by the converter.")

    return pyrauli_circuit
