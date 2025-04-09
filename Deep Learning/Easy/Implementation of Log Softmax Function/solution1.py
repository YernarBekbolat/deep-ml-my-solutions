# https://www.deep-ml.com/problems/39

# pros:
# - shortwritten

# cons:
# - need optimization
# - i really should use lambda here but i'm not sure how to do it so i wont for now 


import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	
	scores_sum = sum(np.e ** (scores[i] - np.max(scores)) for i in range(len(scores)))
	
	return [scores[i] - np.max(scores) - np.log(scores_sum) for i in range(len(scores))]