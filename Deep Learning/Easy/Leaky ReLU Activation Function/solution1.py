# https://www.deep-ml.com/problems/44

# pros:
# - shortwritten

# cons:
# - no any actually
# - just should read this article chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://arxiv.org/pdf/1903.06733

def leaky_relu(z: float, alpha: float = 0.01) -> float|int:
	return z if z > 0 else alpha * z
