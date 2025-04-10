# https://www.deep-ml.com/problems/25

# pros:
# - handwritten code 

# cons:
# - fucking mess
# - can be optimized in speed 

import numpy as np
import math

def sigmoid_function(z: float) -> float:
    return round(1 / (1 + math.e ** -z), 4)

def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
    mse_values = []
    while epochs != 0:    
        probabilities = []
        
        for x in features:
            output = sum(x[i] * initial_weights[i] for i in range(len(x))) + initial_bias
            probabilities.append(sigmoid_function(output))

        mse = round(sum((probabilities[i] - labels[i]) ** 2 for i in range(len(probabilities))) / len(labels), 4)

        mse_values.append(mse)
        
        updated_weights = [round(initial_weights[j] - learning_rate * 2 * sum((probabilities[i] - labels[i]) * (probabilities[i] * (1 - probabilities[i]) * features[i][j]) for i in range(len(probabilities))) / len(labels), 4)
        for j in range(len(initial_weights))]
        initial_weights = updated_weights

        updated_bias = round(initial_bias - learning_rate * 2 * sum((probabilities[i] - labels[i]) * (probabilities[i] * (1 - probabilities[i])) for i in range(len(probabilities))) / len(labels), 4)
        initial_bias = updated_bias
        
        epochs = epochs - 1
    
    return updated_weights, updated_bias, mse_values