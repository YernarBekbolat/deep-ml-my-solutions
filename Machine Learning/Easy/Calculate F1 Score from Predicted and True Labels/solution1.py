# https://www.deep-ml.com/problems/91

# pros:
# - simple and easy to understand

# cons:
# - could make shorter by using numpy built-in functions

def calculate_f1_score(y_true, y_pred):
	"""
	Calculate the F1 score based on true and predicted labels.

	Args:
		y_true (list): True labels (ground truth).
		y_pred (list): Predicted labels.

	Returns:
		float: The F1 score rounded to three decimal places.
	"""
	n_samples = len(y_true)
	true_pos = sum(1 for i in range(n_samples) if y_true[i] == 1 and y_pred[i] == 1)
    false_pos = sum(1 for i in range(n_samples) if y_true[i] == 0 and y_pred[i] == 1)
    false_neg = sum(1 for i in range(n_samples) if y_true[i] == 1 and y_pred[i] == 0)

    precision = true_pos / (true_pos + false_pos) if (true_pos + false_pos) != 0 else 0
    recall = true_pos / (true_pos + false_neg) if (true_pos + false_neg) != 0 else 0

    nominator = precision * recall
    denumerator = precision + recall

    if denumerator == 0.0:
        return 0.0

    f1 = 2 * (nominator / denumerator)

	return round(f1,3)