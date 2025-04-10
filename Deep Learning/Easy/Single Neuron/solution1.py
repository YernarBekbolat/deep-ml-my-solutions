# https://www.deep-ml.com/problems/24

# pros:
# - list comprehensions are cool

# cons:
# - can be optimized in speed 

import math

def sigmoid_function(z: float) -> float:
    return round(1 / (1 + math.e ** -z), 4)

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	probabilities = []
    
    for x in features:
        output = sum(x[i] * weights[i] for i in range(len(x))) + bias
        probabilities.append(sigmoid_function(output))

    mse = sum((probabilities[i] - labels[i]) ** 2 for i in range(len(probabilities))) / len(labels)
    
	return probabilities, mse