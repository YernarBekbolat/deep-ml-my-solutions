# https://www.deep-ml.com/problems/35

# pros:
# - easy to understand

# cons:
# - dont even know if there are any cons

import numpy as np

def make_diagonal(x):
    res = np.zeros((len(x), len(x)))
    
    for i in range(len(x)):
        res[i, i] = x[i]

    return res
