# https://www.deep-ml.com/problems/71

# pros:
# - simple and easy to understand
# - used flatten to work with both 1D and 2D arrays

# cons:
# - could make shorter by using numpy built-in functions

import numpy as np

def rmse(y_true, y_pred):

    y_true = y_true.flatten()
    y_pred = y_pred.flatten()
	
    rmse_res = np.sqrt(sum([(y_true[i] - y_pred[i]) ** 2 for i in range(len(y_true))]) / len(y_true))
    
    return np.round(rmse_res,3)
