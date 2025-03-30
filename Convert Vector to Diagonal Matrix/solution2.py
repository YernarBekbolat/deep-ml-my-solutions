# https://www.deep-ml.com/problems/35

# pros:
# - used manual filling of matrix instead of np.zeros 

# cons:
# - don't see here too

import numpy as np

def make_diagonal(x):
    size = len(x)  
    res = [[0] * size for _ in range(size)]  

    for i in range(size):  
        res[i][i] = x[i]  

    return res
