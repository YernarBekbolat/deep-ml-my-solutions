# https://www.deep-ml.com/problems/97

# pros:
# - easy

# cons:
# - don't see any

import math

def elu(x: float, alpha: float = 1.0) -> float:
	"""
	Compute the ELU activation function.

	Args:
		x (float): Input value
		alpha (float): ELU parameter for negative values (default: 1.0)

	Returns:
		float: ELU activation value
	"""
	if x > 0.0:
        return float(x)
    else:
        return round(alpha * (math.e ** x - 1), 4) 
	