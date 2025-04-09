# https://www.deep-ml.com/problems/27

# pros:
# - uses numpy to solve the problem

# cons:
# - uses numpy to solve the problem!!!!!!!!!!!!!!!!!! I will comeback for native solution some time in the future

import numpy as np

def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
    C_inv = np.linalg.inv(C)  
    P = np.dot(C_inv, B)      
    return P



