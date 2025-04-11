# https://www.deep-ml.com/problems/53

# pros:
# - numpy used
# - optimized in speed and in redundancy 

# cons:
# - don't see so far 

import numpy as np

def softmax(scores: list[float]) -> list[float]:
   return np.exp(scores - np.max(scores)) / sum(np.exp(scores - np.max(scores)))

def compute_qkv(X, W_q, W_k, W_v):
    return np.dot(X, W_q), np.dot(X, W_k), np.dot(X, W_v)

def self_attention(Q, K, V):
    S = np.dot(Q, K.T) / np.sqrt(K.shape[-1])

    A = np.apply_along_axis(softmax, axis=1, arr=S)

    return np.dot(A, V)
