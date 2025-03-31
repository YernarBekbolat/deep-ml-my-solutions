# pros: 
# - transpose used for column mode

# cons:
# - built-in function used for column mode
# O(n^2) time complexity

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    
    means = []
    if mode == 'row':
        for row in matrix:
            total = 0
            for i in range(len(row)):
                total += row[i]
            means.append(total / len(row))

    if mode == 'column':
        matrix = zip(*matrix)
        for col in matrix:
            total = 0
            for i in range(len(col)):
                total += col[i]
            means.append(total / len(col))

	return means