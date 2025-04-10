# https://www.deep-ml.com/problems/14

# pros:
# - clean and readable. @ used, should remember it

# cons:
# - don't see so far 

import numpy as np
from numpy.linalg import inv

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	X = np.array(X)
    y = np.array(y)

    theta = inv(X.T @ X) @ X.T @ y
	return theta