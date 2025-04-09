# https://www.deep-ml.com/problems/66

# pros:
# - uses zip to iterate over the vectors
# - uses list comprehension 
# - badass one-liner

# cons:
# - don't see so far

def dot_product(a, b):
    if len(a) != len(b):
        return None

    # return sum(a[i] * b[i] for i in range(len(a)))
    return sum(x * y for x, y in zip(a, b))


def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
    return list(((dot_product(v, L) / dot_product(L, L)) * i for i in L))
	
