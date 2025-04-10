# https://www.deep-ml.com/problems/99

# pros:
# - easy

# cons:
# - don't see any

import math

def softplus(x: float) -> float:
	"""
	Compute the softplus activation function.

	Args:
		x: Input value

	Returns:
		The softplus value: log(1 + e^x)
	"""
	return round(math.log(1 + math.e ** x), 4)