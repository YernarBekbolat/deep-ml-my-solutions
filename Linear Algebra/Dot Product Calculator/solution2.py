
# https://www.deep-ml.com/problems/83

# pros:
# - sick one-liner

# cons:
# - don't see lol

import numpy as np

def calculate_dot_product(vec1, vec2) -> float:
	"""
	Calculate the dot product of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	"""
    return sum(vec1[i] * vec2[i] for i in range(len(vec1)))