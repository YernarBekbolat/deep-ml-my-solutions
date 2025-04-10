# https://www.deep-ml.com/problems/98

# pros:
# - easy

# cons:
# - don't see any

def prelu(x: float, alpha: float = 0.25) -> float:
	"""
	Implements the PReLU (Parametric ReLU) activation function.

	Args:
		x: Input value
		alpha: Slope parameter for negative values (default: 0.25)

	Returns:
		float: PReLU activation value
	"""
	return x if x > 0.0 else alpha * x