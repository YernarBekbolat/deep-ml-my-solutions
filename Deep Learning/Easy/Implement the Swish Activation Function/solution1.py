# https://www.deep-ml.com/problems/102

# pros:
# - easy

# cons:
# - don't see any

import math

def swish(x: float) -> float:
	"""
	Implements the Swish activation function.

	Args:
		x: Input value

	Returns:
		The Swish activation value
	"""
    return x * (1 / (1 + math.e ** -x))