# examples/qiskit_backend.py
import math
import numpy as np

try:
    from qiskit.circuit import QuantumCircuit, Parameter
    from qiskit.quantum_info import SparsePauliOp
    from pyrauli import PBackend
except ImportError:
    print("Please install pyrauli with Qiskit support: pip install 'pyrauli[qiskit]'")
    exit()

def main():
    """
    Demonstrates how to use the PBackend with Qiskit, including parameterized circuits.
    """
    # --- Part 1: Simple Bell State ---
    print("--- 1. Creating and running a Bell state circuit ---")
    
    qc_bell = QuantumCircuit(2, name="bell_state")
    qc_bell.h(0)
    qc_bell.cx(0, 1)
    
    # Define observables to measure
    obs_z = SparsePauliOp("ZI")
    obs_x = SparsePauliOp("XI")
    
    # Instantiate the pyrauli backend
    backend = PBackend()
    
    # Create the PUB: (circuit, observables)
    bell_pub = (qc_bell, [obs_z, obs_x])
    
    print("\nRunning Bell state circuit...")
    job = backend.run([bell_pub])
    result = job.result()
    
    # The 'evs' (expectation values) are in the first PubResult's data
    exp_values = result.results[0].data.evs
    
    print(f"Expectation value for ZI: {exp_values[0]:.6f}")
    print(f"Expectation value for XI: {exp_values[1]:.6f}")

    # --- Part 2: Parameterized Circuit ---
    print("\n--- 2. Creating and running a parameterized circuit ---")
    
    # Create a circuit with a parameter
    theta = Parameter('θ')
    qc_param = QuantumCircuit(1, name="param_circ")
    qc_param.h(0)
    qc_param.rz(theta, 0)
    
    obs_y = SparsePauliOp("Y")
    
    # Define the parameter values to sweep over
    theta_values = np.linspace(0, 2 * np.pi, 5)
    
    # Create a list of PUBs, one for each parameter value
    param_pubs = []
    for val in theta_values:
        # PUB format: (circuit, observable, parameter_values)
        param_pubs.append((qc_param, obs_y, [val]))
        
    print(f"\nRunning parameterized circuit for {len(theta_values)} values of theta...")
    param_job = backend.run(param_pubs)
    param_result = param_job.result()
    
    print("Expectation value of Y for different theta:")
    for i, pub_result in enumerate(param_result.results):
        theta_val = theta_values[i]
        exp_val = pub_result.data.evs[0]
        print(f"  θ = {theta_val:.4f}, <Y> = {exp_val:.6f}")

if __name__ == "__main__":
    main()
