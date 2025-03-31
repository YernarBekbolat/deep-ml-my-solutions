
# https://www.deep-ml.com/problems/84

# pros:
# one-liner with a proper output

# cons:
# don't see so far

import numpy as np

def phi_transform(data: list[float], degree: int) -> list[list[float]]:
	"""
	Perform a Phi Transformation to map input features into a higher-dimensional space by generating polynomial features.

	Args:
		data (list[float]): A list of numerical values to transform.
		degree (int): The degree of the polynomial expansion.

	"""
    return list([x ** j for j in range(degree + 1)] for x in data)