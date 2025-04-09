# https://www.deep-ml.com/problems/84

# pros:
# very simple and easy to understand

# cons:
# not efficient for large datasets

import numpy as np

def phi_transform(data: list[float], degree: int) -> list[list[float]]:
	"""
	Perform a Phi Transformation to map input features into a higher-dimensional space by generating polynomial features.

	Args:
		data (list[float]): A list of numerical values to transform.
		degree (int): The degree of the polynomial expansion.

	"""
    res = []

    for i in data:
        for j in range(0, degree + 1):
            res.append(i ** j) 

    return res