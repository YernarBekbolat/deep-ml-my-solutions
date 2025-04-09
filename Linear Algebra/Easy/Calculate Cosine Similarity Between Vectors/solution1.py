# https://www.deep-ml.com/problems/76   

# pros:
# - easy to understand, compact code

# cons:
# - don't see lol, but could be more readable and added error handling

import numpy as np

def cosine_similarity(v1, v2):
	if len(v1) != len(v2):
        return

    dot_product = sum(v1[i] * v2[i] for i in range(len(v1)))

    l2_v1 = sum(v1[i] ** 2 for i in range(len(v1))) ** 0.5
    l2_v2 = sum(v2[i] ** 2 for i in range(len(v2))) ** 0.5

    return round(dot_product / (l2_v1 * l2_v2), 3)
