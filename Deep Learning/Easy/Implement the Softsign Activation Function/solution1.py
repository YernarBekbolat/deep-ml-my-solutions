# https://www.deep-ml.com/problems/100

# pros:
# - easy

# cons:
# - don't see any

def softsign(x: float) -> float:
	"""
	Implements the Softsign activation function.

	Args:
		x (float): Input value

	Returns:
		float: The Softsign of the input	"""
	# Your code here
	return round(x / (1 + abs(x)), 4)