# https://www.deep-ml.com/problems/61

# pros:
# - easy

# cons:
# - as always, should optimize the speed
# - didnt included special cases 

import numpy as np

def f_score(y_true, y_pred, beta):
	"""
	Calculate F-Score for a binary classification task.

	:param y_true: Numpy array of true labels
	:param y_pred: Numpy array of predicted labels
	:param beta: The weight of precision in the harmonic mean
	:return: F-Score rounded to three decimal places
	"""
    true_pos = sum(1 for i in range(len(y_pred)) if y_pred[i] == 1 and y_true[i] == 1)
    false_pos = sum(1 for i in range(len(y_pred)) if y_pred[i] == 1 and y_true[i] == 0)
    false_neg = sum(1 for i in range(len(y_true)) if y_true[i] == 1 and y_pred[i] == 0)

    precision = true_pos / (true_pos + false_pos)
    recall = true_pos / (true_pos + false_neg)

    return round((1 + beta ** 2) * ((precision * recall) / ((beta ** 2 * precision) + recall)), 3)
