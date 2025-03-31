# https://www.deep-ml.com/problems/65

# pros:
# - uses enumerate to get the index of the non-zero value and basically it's faster then using range()

# cons:
# - don't see so far


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
        for j, value in enumerate(row):
            if value != 0:
                vals.append(value)
                col_idx.append(j)
        row_ptr.append(len(vals))

    return vals, col_idx, row_ptr
        


