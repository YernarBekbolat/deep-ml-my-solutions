# https://www.deep-ml.com/problems/25

# pros:
# - readable and understandable
# - numpy used
# - optimized in speed and in redundancy 

# cons:
# - don't see so far 

import math
import numpy as np

def sigmoid(z: float) -> float:
    return 1 / (1 + math.exp(-z))

def sigmoid_derivative(prob: float) -> float:
    return prob * (1 - prob)

def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	weights = initial_weights.copy()
    bias = initial_bias
    mse_values = []

    for epoch in range(epochs):
        linear_output = np.dot(features, weights) + bias
        probabilities = np.array([sigmoid(z) for z in linear_output])

        errors = probabilities - labels
        mse = np.mean(errors ** 2)
        mse_values.append(mse)

        sigmoid_grads = sigmoid_derivative(probabilities)
        gradients = errors * sigmoid_grads

        for j in range(len(weights)):
            grad_wj = np.mean(gradients * features[:, j])
            weights[j] -= learning_rate * 2 * grad_wj

        grad_b = np.mean(gradients)
        bias -= learning_rate * 2 * grad_b

	return weights, bias, mse_values