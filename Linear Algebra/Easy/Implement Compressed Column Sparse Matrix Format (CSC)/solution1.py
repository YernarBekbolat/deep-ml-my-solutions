# https://www.deep-ml.com/problems/67

# pros:
# more smart way to iterate over the matrix

# cons:
# don't see so far

def compressed_col_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix into its Compressed Column Sparse (CSC) representation.

	:param dense_matrix: List of lists representing the dense matrix
	:return: Tuple of (values, row indices, column pointer)
	"""
	vals = []
	row_idx = []
	col_ptr = [0]

	num_rows = len(dense_matrix)
	num_cols = len(dense_matrix[0])

	for col_index in range(num_cols):
		for row_index in range(num_rows):
			if dense_matrix[row_index][col_index] != 0:
				vals.append(dense_matrix[row_index][col_index])
				row_idx.append(row_index)
		col_ptr.append(len(vals))

	return vals, row_idx, col_ptr
