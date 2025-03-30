# pros:
# - no built-in function used

# cons:
# - still O(n^2) time complexity but meh, it's still looks more readable than solution1

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    means = []
    
    if mode == 'row':
        for row in matrix:
            total = sum(row)  
            means.append(total / len(row))
    
    elif mode == 'column':
        num_rows = len(matrix)
        num_cols = len(matrix[0]) if matrix else 0  
        
        for col_index in range(num_cols):  
            total = 0
            for row in matrix:  
                total += row[col_index]
            means.append(total / num_rows)
    
    return means
