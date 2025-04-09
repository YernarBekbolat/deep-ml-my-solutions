# https://www.deep-ml.com/problems/69

# pros:
# - easy

# cons:
# - as always, should optimize the speed

import numpy as np

def r_squared(y_true, y_pred):
	# Write your code here
    ssr = sum(np.square(y_true[i] - y_pred[i]) for i in range(len(y_true)))

    y_mean = np.mean(y_true)

    sst = sum(np.square(y_true[i] - y_mean) for i in range(len(y_true)))

    return 1 - (ssr / sst)
