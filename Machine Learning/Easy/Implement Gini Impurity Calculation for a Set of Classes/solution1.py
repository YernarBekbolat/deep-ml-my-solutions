# https://www.deep-ml.com/problems/64

# pros:
# - used unique to get the counts of each class

# cons:
# - as always, should optimize the speed

import numpy as np

def gini_impurity(y):
	"""
	Calculate Gini Impurity for a list of class labels.

	:param y: List of class labels
	:return: Gini Impurity rounded to three decimal places
	"""
    n = len(y)
    if n == 0:
        return 0.0

    _, counts = np.unique(y, return_counts = True)
    probs = counts / n
    val = 1 - sum(probs ** 2) 
	return round(val,3)