# https://www.deep-ml.com/problems/76

# pros:
# - more readable, added error handling, zip used for vectors 

# cons:
# - not true, true software wouldnt use zip

import numpy as np

def cosine_similarity(v1, v2):
    if len(v1) != len(v2):
        return None  

    dot_product = sum(x * y for x, y in zip(v1, v2))
    
    l2_v1 = sum(x ** 2 for x in v1) ** 0.5
    l2_v2 = sum(y ** 2 for y in v2) ** 0.5

    if l2_v1 == 0 or l2_v2 == 0:
        return None  

    return round(dot_product / (l2_v1 * l2_v2), 3)
