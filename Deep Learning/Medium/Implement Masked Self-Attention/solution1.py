# https://www.deep-ml.com/problems/107

# pros:
# - numpy used
# - optimized in speed and in redundancy 

# cons:
# - don't see so far 

import numpy as np

def softmax(scores: list[float]) -> list[float]:
    return np.exp(scores - np.max(scores)) / np.sum(np.exp(scores - np.max(scores)))

def compute_qkv(X: np.ndarray, W_q: np.ndarray, W_k: np.ndarray, W_v: np.ndarray):
	"""
	Compute Query (Q), Key (K), and Value (V) matrices.
	"""
	return np.dot(X, W_q), np.dot(X, W_k), np.dot(X, W_v)

def masked_attention(Q: np.ndarray, K: np.ndarray, V: np.ndarray, mask: np.ndarray) -> np.ndarray:
	"""
	Compute masked self-attention.
	"""
	S = np.dot(Q, K.T) / np.sqrt(K.shape[-1])
    
    A = np.apply_along_axis(softmax, axis = 1, arr = S + mask)

    return np.dot(A, V)