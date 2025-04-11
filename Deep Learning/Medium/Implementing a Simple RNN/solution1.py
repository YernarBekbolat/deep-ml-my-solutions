# https://www.deep-ml.com/problems/54

# pros:
# - numpy used
# - optimized in speed and in redundancy 

# cons:
# - don't see so far 

import numpy as np

def tanh(x: float) -> float:
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

def rnn_forward(input_sequence: list[list[float]], initial_hidden_state: list[float], Wx: list[list[float]], Wh: list[list[float]], b: list[float]) -> list[float]:
    h_prev = initial_hidden_state
	for t in range(len(input_sequence)):
        x_t = input_sequence[t]

        h_t = tanh(np.dot(Wx, x_t) + np.dot(Wh, h_prev) + b)

        h_prev = h_t
	
    return h_prev