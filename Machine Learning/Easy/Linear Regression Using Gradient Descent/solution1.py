# https://www.deep-ml.com/problems/15

# pros:
# - numpy used
# - optimized in speed and in redundancy 

# cons:
# - don't see so far 

import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
	# Your code here, make sure to round
    X = np.array(X)
    y = np.array(y)
    
    m, n = X.shape
    y = y.reshape(m, 1)
	theta = np.zeros((n, 1))

    for iteration in range(iterations):
        y_pred = X @ theta
        error = y_pred - y
        grad = (X.T @ error) / m
        theta -= alpha * grad

	return theta