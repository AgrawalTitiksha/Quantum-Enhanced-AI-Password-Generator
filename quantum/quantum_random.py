from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

def generate_quantum_bits(n_bits=16):
    qc = QuantumCircuit(n_bits, n_bits)
    qc.h(range(n_bits))
    qc.measure(range(n_bits), range(n_bits))

    backend = Aer.get_backend('qasm_simulator')
    job = backend.run(transpile(qc, backend), shots=1)
    result = job.result()
    counts = result.get_counts()
    binary_str = list(counts.keys())[0]
    return binary_str
