# Quantum Space Invaders

Quantum Space Invaders is a repository containing a simple python implementation of the game Space Invaders with a twist: random number generation is performed through the emulation of a quantum computer.

## Description

As stated before, the implementation of the Space Invaders game is simple. But we apply the concept of quantum indeterminancy through a (simulated) quantum computer for random number generation.

The generated random number will then be used to determine the horizontal position of a newly spawned alien, therefore we need a number of qubits that can represent the number of potential positions. See below an example of quantum circuit with 3 qubits that can provide random outputs between 0 and 7.

```
     ┌───┐┌─┐      
q_0: ┤ H ├┤M├──────
     ├───┤└╥┘┌─┐
q_1: ┤ H ├─╫─┤M├───
     ├───┤ ║ └╥┘┌─┐
q_2: ┤ H ├─╫──╫─┤M├
     └───┘ ║  ║ └╥┘
c: 3/══════╩══╩══╩═
           0  1  2
```

This circuit applies a Hadamard gate to each qubit, which will cause an equal probability of states that, after measurement, will translate into a uniform probability of each potential value (see Hadamard gate matrix below).

$$ {\frac{1}{\sqrt{2}}} \begin{bmatrix} 1&1 \\\ 1&-1 \end{bmatrix} $$

## Installation

To use this project you just need a python interpreter equal or superior to v3.13 and an associated pip package installer. Afterwards, you may use the following command to install all python dependencies:

```
pip install -r requirements.txt
```

## Usage

In order to execute the Space Invaders impletation you just need to run:
```
python main.py
```

This will open a new window that you may start using inmediatly.

You may also use the quantum random number generator in other projects by importing it:
```
from quantum.quantum_rng import QuantumRng
[...]
random_number_generator = QuantumRng(qbits=3,backend="your_peferred_backend", api_key="your_api_key")
random_number = random_number_generator.generate()
```

The default and recommended backend is Aer's qasm_simulator (that doesn't require an API key), but the code is also compatible with the IBM Runtime Client.

It is also posible to modify the backend, number of qubits and so forth, by editing the variables defined in [space_invaders/settings.py](/space_invaders/settings.py) to use them while playing Space Invaders. But it is highly recommended to keep using the qasm_simulator to save (a large sum of) money.