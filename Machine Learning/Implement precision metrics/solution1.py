# https://www.deep-ml.com/problems/46

# pros:
# - simple and easy to understand

# cons:
# - didn't use numpy

import numpy as np

def precision(y_true, y_pred):
	true_pos = sum(1 for i in range(len(y_pred)) if y_pred[i] == 1 and y_true[i] == 1)
    false_pos = sum(1 for i in range(len(y_pred)) if y_pred[i] == 1 and y_true[i] == 0)

    return true_pos / (true_pos + false_pos)
