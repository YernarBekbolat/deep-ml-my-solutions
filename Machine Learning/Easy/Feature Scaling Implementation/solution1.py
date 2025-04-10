# https://www.deep-ml.com/problems/16

# pros:
# - numpy used
# - optimized in speed and in redundancy 

# cons:
# - don't see so far 

import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    standardized_data = (data - np.mean(data, axis = 0)) / np.std(data, axis=0)

    normalized_data = (data - np.min(data, axis=0)) / (np.max(data, axis=0) - np.min(data, axis=0))

	return standardized_data, normalized_data