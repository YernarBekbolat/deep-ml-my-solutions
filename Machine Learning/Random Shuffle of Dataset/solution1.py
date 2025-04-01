# https://www.deep-ml.com/problems/29

# pros:
# - simple and easy to understand
# - numpy is fast as hell

# cons:
# - will find the native solution in the future


import numpy as np

def shuffle_data(X, y, seed=None):
    if seed is not None:
        np.random.seed(seed)

	indices = np.random.permutation(len(X))  
    return X[indices], y[indices]