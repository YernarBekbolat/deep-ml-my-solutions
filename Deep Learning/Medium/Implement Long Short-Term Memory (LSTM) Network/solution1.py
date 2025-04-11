# https://www.deep-ml.com/problems/59

# pros:
# - numpy used
# - optimized in speed and in redundancy 

# cons:
# - don't see so far 


import numpy as np

def tanh(x: float) -> float:
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

def sigmoid(z: float) -> float:
	return 1 / (1 + np.exp(-z))

class LSTM:
	def __init__(self, input_size, hidden_size):
		self.input_size = input_size
		self.hidden_size = hidden_size

		# Initialize weights and biases
		self.Wf = np.random.randn(hidden_size, input_size + hidden_size)
		self.Wi = np.random.randn(hidden_size, input_size + hidden_size)
		self.Wc = np.random.randn(hidden_size, input_size + hidden_size)
		self.Wo = np.random.randn(hidden_size, input_size + hidden_size)

		self.bf = np.zeros((hidden_size, 1))
		self.bi = np.zeros((hidden_size, 1))
		self.bc = np.zeros((hidden_size, 1))
		self.bo = np.zeros((hidden_size, 1))

	def forward(self, x, initial_hidden_state, initial_cell_state):
    """
    Processes a sequence of inputs and returns the hidden states, final hidden state, and final cell state.
    """
    outputs = []
    
    h_prev = initial_hidden_state
    c_prev = initial_cell_state

    for t in range(len(x)):
        x_t = x[t].reshape(-1, 1)
        
        h_prev = h_prev.reshape(self.hidden_size, 1)
        c_prev = c_prev.reshape(self.hidden_size, 1)

        concat = np.vstack((h_prev, x_t))

        f_t = sigmoid(np.dot(self.Wf, concat) + self.bf)
        i_t = sigmoid(np.dot(self.Wi, concat) + self.bi)
        c_tilda = tanh(np.dot(self.Wc, concat) + self.bc)
        
        c_t = f_t * c_prev + i_t * c_tilda

        o_t = sigmoid(np.dot(self.Wo, concat) + self.bo)
        
        h_t = o_t * tanh(c_t)

        outputs.append(h_t)

        h_prev = h_t
        c_prev = c_t

    return outputs, h_prev, c_prev
