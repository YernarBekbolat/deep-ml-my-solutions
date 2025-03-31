# https://www.deep-ml.com/problems/65

# pros:
# - efficient for sparse matrices
# - easy to understand
# - easy to implement

# cons:
# - shitty code basically


import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix to its Compressed Row Sparse (CSR) representation.

	:param dense_matrix: 2D list representing a dense matrix
	:return: A tuple containing (values array, column indices array, row pointer array)
	"""
    vals = []
    col_idx = []
    row_ptr = [0]
	
    for row in dense_matrix:
        for i in range(len(row)):
            if row[i] != 0:
                vals.append(row[i])
                col_idx.append(i)
        row_ptr.append(len(vals))

    return vals, col_idx, row_ptr


