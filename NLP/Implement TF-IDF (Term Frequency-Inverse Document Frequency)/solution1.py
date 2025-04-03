# https://www.deep-ml.com/problems/60

# pros:
# - sexy code

# cons:
# - need to be fastened 
# - no L2 normalization

import numpy as np

def compute_tf_idf(corpus, query):
	"""
	Compute TF-IDF scores for a query against a corpus of documents.
    
	:param corpus: List of documents, where each document is a list of words
	:param query: List of words in the query
	:return: List of lists containing TF-IDF scores for the query words in each document
	"""
    df_dict = {word: sum(1 for doc in corpus if word in doc) for word in query}
    idf_dict = {word: np.log((len(corpus) + 1) / ((df_dict[word]) + 1)) + 1 for word in query}
    
    tf_idf = [ 
        [((doc.count(word) / len(doc)) * idf_dict[word]) if word in doc else 0.0 for word in query]
        for doc in corpus
    ]
    
    return tf_idf
    

   
    
