# https://www.deep-ml.com/problems/5

# pros:
# - simple and easy to understand

# cons:
# - O(n^2) time complexity

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	
    result = []
    for row in matrix:
        for i in range(len(row)):
            result.append(row[i] * scalar)
    
    return result