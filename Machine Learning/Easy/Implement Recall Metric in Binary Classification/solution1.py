# https://www.deep-ml.com/problems/52

# pros:
# - simple and easy to understand
# - used sum to count the number of true positives and false negatives

# cons:
# - could make shorter by using numpy built-in functions

import numpy as np

def recall(y_true, y_pred):
    true_pos = sum(1 for i in range(len(y_true)) if y_true[i] == 1 and y_pred[i] == 1)
    false_neg = sum(1 for i in range(len(y_true)) if y_true[i] == 1 and y_pred[i] == 0)

    return round(true_pos / (true_pos + false_neg), 3)
