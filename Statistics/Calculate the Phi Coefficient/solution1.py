# https://www.deep-ml.com/problems/95

# pros:
# - nice way to iterate over the lists and count without many lines of code

# cons:
# - don't see so far

def phi_corr(x: list[int], y: list[int]) -> float:
	"""
	Calculate the Phi coefficient between two binary variables.

	Args:
	x (list[int]): A list of binary values (0 or 1).
	y (list[int]): A list of binary values (0 or 1).

	Returns:
	float: The Phi coefficient rounded to 4 decimal places.
	"""
	# Your code here
	x_00 = sum(1 for i in range(len(x)) if x[i] == 0 and y[i] == 0)
   
    x_01 = sum(1 for i in range(len(x)) if x[i] == 0 and y[i] == 1)
   
    x_10 = sum(1 for i in range(len(x)) if x[i] == 1 and y[i] == 0)
    
    x_11 = sum(1 for i in range(len(x)) if x[i] == 1 and y[i] == 1)
  

    numerator = (x_00 * x_11) - (x_01 * x_10)
    denominator = ((x_00 + x_01) * (x_10 + x_11) * (x_00 + x_10) * (x_01 + x_11)) ** 0.5

    val = numerator / denominator if denominator != 0 else 0.0

	return round(val,4)