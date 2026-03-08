import qiskit
from qiskit_aer import Aer
from qiskit_ibm_runtime import SamplerV2, QiskitRuntimeService


class QuantumRng:
    def __init__(self, qbits, backend, api_key=""):
        self.circuit = qiskit.QuantumCircuit(qbits, qbits)
        for i in range(qbits):
            self.circuit.h(i)
        self.circuit.measure(list(range(qbits)), list(range(qbits)))
        if backend in [b.name for b in Aer.backends()]:
            self.backend = Aer.get_backend(backend)
            self.is_remote = False
        else:
            service = QiskitRuntimeService(channel="ibm_quantum", token=api_key)
            self.backend = service.backend(backend)
            self.sampler = SamplerV2(self.backend)
            self.is_remote = True

    def generate(self):
        if self.is_remote:
            job = self.sampler.run([self.circuit], shots=1)
            result = job.result()[0]
            bit_string = result.data.c.get_bitstrings()[0]
        else:
            job = self.backend.run(self.circuit, shots=1)
            result = job.result()
            counts = result.get_counts()
            bit_string = list(counts.keys())[0]
        
        return int(bit_string, 2)

