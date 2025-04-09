# https://www.deep-ml.com/problems/93

# pros:
# - simple and easy to understand

# cons:
# - shall not use flatten i guess

import numpy as np

def mae(y_true, y_pred):
	"""
	Calculate Mean Absolute Error between two arrays.

	Parameters:
	y_true (numpy.ndarray): Array of true values
    y_pred (numpy.ndarray): Array of predicted values

	Returns:
	float: Mean Absolute Error rounded to 3 decimal places
	"""

    y_true = y_true.flatten()
    y_pred = y_pred.flatten()

	n = len(y_pred)

    val = sum([abs(y_true[i] - y_pred[i]) for i in range(n)]) / n

	return round(float(val), 3)
    # return val