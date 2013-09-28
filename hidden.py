

class HMM:
	""" 
	Represents a basic Hidden Markov Model.
	
	Parameters:
	 - states: tuple of states
	 - observations: tuple of observations
	 - state_transitions: dictionary of ((state_i, state_k), probability) pairs
	 - observ_transitions: dictionary of ((state_i, observation_k), probability) pairs
	 - p_initial: initial probabilities of states; dictionary of (state_i, probability_i) pairs
	
	This class can be initialised either by a set of parameters, 
	or by an observation sequence, in which case a model that is trained with this sequence is generated.
	"""
	def __init__(self, *args): 
		if len(args) == 1: self.from_sequence(*args)
		elif len(args) == 5: self.from_states(*args)


	def from_states(self, states, observations, state_transitions, observ_transitions, p_initial):
		self.states = states
		self.observations = observations
		self.state_transitions = state_transitions
		self.observ_transitions = observ_transitions
		self.p_initial = p_initial

	def from_sequence(self, osequence):
		self.train(osequence)

	""" 
	Determines the probability that with the given HMM, 
	the hidden state at the end of the given observation sequence is exactly state.

	
	"""
	def filter (self, osequence, state):
		pass


	""" 
	Determines the most likely sequence of hidden states, given the observations in osequence.
	"""
	def decode(self, osequence):
		pass	


	"""
	Trains the current HMM with a given sequence of observations.
	"""
	def train(self, osequence):
		pass
