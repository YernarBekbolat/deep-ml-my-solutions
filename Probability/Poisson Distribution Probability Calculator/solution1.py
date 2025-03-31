# https://www.deep-ml.com/problems/81

# pros:
# - easy implementation

# cons:
# - don't see so far

import math

def poisson_probability(k, lam):
	"""
	Calculate the probability of observing exactly k events in a fixed interval,
	given the mean rate of events lam, using the Poisson distribution formula.
	:param k: Number of events (non-negative integer)
	:param lam: The average rate (mean) of occurrences in a fixed interval
	"""
	# Your code here
	val = (lam ** k * math.e ** -lam) / math.factorial(k)
	return round(val,5)