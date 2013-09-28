

class HMM:
	""" 
	Represents a basic Hidden Markov Model.
	
	Parameters:
	 - states: tuple of states
	 - observations: tuple of observations
	 - state_transitions: dictionary of ((state_i, state_k), probability) pairs
	 - observ_transitions: dictionary of ((state_i, observation_k), probability) pairs
	 - p_initial: initial probabilities of states; dictionary of (state_i, probability_i) pairs
	
	
	"""
	def __init__(self, states, observations, state_transitions, observ_transitions, p_initial):
		self.states = states
		self.observations = observations
		self.state_transitions = state_transitions
		self.observ_transitions = observ_transitions
		self.p_initial = p_initial


	
