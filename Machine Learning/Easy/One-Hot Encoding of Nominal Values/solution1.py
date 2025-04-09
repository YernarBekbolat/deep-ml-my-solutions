# https://www.deep-ml.com/problems/34

# pros:
# - simple and easy to understand

# cons:
# - this solution should be studied more...

import numpy as np

def to_categorical(x, n_col=None):
    if n_col is None:
        n_col = x.max() + 1

	n_rows = len(x)
    res = np.zeros((n_rows, n_col))

    for i in range(n_rows):
        res[i, x[i]] = 1

    return res