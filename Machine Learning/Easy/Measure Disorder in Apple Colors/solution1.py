# https://www.deep-ml.com/problems/108

# pros:
# - used unique to get the counts of each class

# cons:
# - as always, should optimize the speed

import numpy as np

def gini_impurity(y) -> float:
    n = len(y)
    if n == 0:
        return 0.0

    _, counts = np.unique(y, return_counts = True)
    probs = counts / n
    return 1 - sum(probs ** 2)


def disorder(apples: list) -> float:
	"""
	Compute the disorder in a basket of apples.
	"""
	return gini_impurity(apples)