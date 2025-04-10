# https://www.deep-ml.com/problems/19

# pros:
# - numpy used
# - optimized in speed and in redundancy 

# cons:
# - don't see so far 

import numpy as np 
from numpy.linalg import eig

def pca(data: np.ndarray, k: int) -> np.ndarray:
	data = (data - np.mean(data, axis = 0)) / np.std(data, axis=0)

    cov = np.dot(data.T, data) / (len(data) - 1)

    eigenvalues, eigenvectors = eig(cov)

    sorted_indices = np.argsort(eigenvalues)[::-1]

    sorted_eigenvalues = eigenvalues[sorted_indices]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]

    principal_components = sorted_eigenvectors[:, :k]

	return np.round(principal_components, 4)
    