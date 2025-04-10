# https://www.deep-ml.com/problems/103

# pros:
# - easy

# cons:
# - don't see any

import math

def selu(x: float) -> float:
	"""
	Implements the SELU (Scaled Exponential Linear Unit) activation function.

	Args:
		x: Input value

	Returns:
		SELU activation value
	"""
	alpha = 1.6732632423543772
	scale = 1.0507009873554804
	return scale * x if x > 0.0 else scale * alpha * (math.e ** x - 1)