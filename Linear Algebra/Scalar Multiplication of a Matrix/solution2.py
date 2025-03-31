# https://www.deep-ml.com/problems/5

# pros:
# - concise and elegant, list comprehension used, more pythonic

# cons:
# - still O(n^2) time complexity

def scalar_multiply(matrix: list[list[int | float]], scalar: int | float) -> list[list[int | float]]:
    return [[elem * scalar for elem in row] for row in matrix]
