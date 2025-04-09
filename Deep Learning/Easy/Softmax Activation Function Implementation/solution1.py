# https://www.deep-ml.com/problems/23

# pros:
# - easy

# cons:
# - don't see any

import math

def softmax(scores: list[float]) -> list[float]:
    denom = sum(math.e ** scores[i] for i in range(len(scores)))

    probabilities = [(math.e ** scores[i]) / denom for i in range(len(scores))]
	
    return probabilities