# https://www.deep-ml.com/problems/24

# pros:
# - numpy used
# - optimized in speed and in redundancy 

# cons:
# - don't see so far 

import math
import numpy as np

def sigmoid(z: float) -> float:
    return 1 / (1 + math.exp(-z))

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	linear_output = np.dot(features, weights) + bias
    probabilities = np.array([sigmoid(z) for z in linear_output])

    errors = probabilities - labels
    mse = np.mean(errors ** 2)

	return probabilities, mse