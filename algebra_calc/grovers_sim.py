# %%
import matplotlib.pyplot as plt
import numpy as np
<<<<<<< HEAD
from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram

# %%
tok = "jlyh1s8MpG-5fsBsZ3bL87-B_cdjIeSJBqA9C5RNMdxu"

# %% function definition
def Initialize(QC,qubits):
    for q in qubits:
        QC.h(q)
    return QC

# %% create a quantum circuit
n = 2 # number of qubits
grover_circuit = QuantumCircuit(n)
grover_circuit = Initialize(grover_circuit, [0, 1])

# oracle 
grover_circuit.cz(0, 1)  # apply a controlled-Z gate

# diffusion operator
grover_circuit.h([0,1])  # apply Hadamard gate to the first qubit
grover_circuit.z([0,1])  # apply X gate to the first qubit
grover_circuit.cz(0, 1)  # apply a controlled-Z gate
grover_circuit.h([0,1])  # apply Hadamard gate to the first qubit

# %% show the circuit
grover_circuit.draw(output='mpl',filename="grover_init.png")


# %% simulate the circuit
backend = Aer.get_backend('statevector_simulator')
job_sim = backend.run(grover_circuit, shots=1024)
state_vector = job_sim.result().get_statevector()

# measure the state vector
grover_circuit.measure_all()
quasm_simulator = Aer.get_backend('qasm_simulator')
results = quasm_simulator.run(grover_circuit, shots=1024).result()

plot_histogram(results.get_counts())



# %% loading the provider and the backend
provider = QiskitRuntimeService(channel='ibm_quantum_platform',token=tok,)
device = provider.least_busy(min_num_qubits=n,operational=True, simulator=False)

print(f"Running on {device.name} with {-1} qubits")
# %% run the circuit on the device
sampler = Sampler(device)
job = sampler.run([grover_circuit])
results = job.result()

plot_histogram(results.get_counts(grover_circuit))
=======
import qiskit as q
>>>>>>> efd3e822df3ec5a3761728b68a594214429fec6d
