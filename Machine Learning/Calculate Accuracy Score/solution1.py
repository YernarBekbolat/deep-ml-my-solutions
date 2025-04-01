# https://www.deep-ml.com/problems/36

# pros:
# - simple and easy to understand

# cons:
# - didn't use numpy

import numpy as np

def accuracy_score(y_true, y_pred):
	if len(y_true) != len(y_pred):
        return None

    num_of_cor_pred = sum(1 for i in range(len(y_true)) if y_true[i] == y_pred[i])

    return num_of_cor_pred / len(y_pred)