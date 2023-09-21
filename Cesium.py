# simulate a Cesium atom to make a clock that is accurate to the nanosecond use qiskit

# import modules
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer
from qiskit.visualization import plot_histogram
import time
import pylatexenc
import qiskit_aer as aer

# define the quantum and classical registers use
q = QuantumRegister(1)
c = ClassicalRegister(1)

# define the quantum circuit
qc = QuantumCircuit(q, c)

# apply the hadamard gate
qc.h(q[0])

# measure the qubit
qc.measure(q, c)

# draw the circuit
qc.draw(output='mpl')

# execute the circuit
job = execute(qc, backend=Aer.get_backend('qasm_simulator'), shots=1)

# get the result
result = job.result()

# get the counts
counts = result.get_counts(qc)

# print the counts
print(counts)

# get the time
current_time = time.time()

# calculate the number of seconds since the epoch
seconds_since_epoch = int(current_time)

# calculate the number of nanoseconds within the current second
nanoseconds = int((current_time - seconds_since_epoch) * 1e9)

# print the current time in seconds and nanoseconds
print(f"Seconds since epoch: {seconds_since_epoch}")

# print the nanoseconds
print(f"Nanoseconds: {nanoseconds}")

# plot the histogram
plot_histogram(counts)

# print the time
print(time.time())

# print the time
print(time.time_ns())

# print circuit
print(qc)

# main function plot the histogram and print the circuit
if __name__ == '__main__':
    plot_histogram(counts)
    print(qc)

