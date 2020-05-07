from dialogue_state import *

class MultiWOZDataFrame:
	def __init__(self, id):
		self.id = id
		self.__domains = ''
		self.__dialogue_state_list = []
		self.__dialogue_acts_list = []
	
	def set_domains(self, domains):
		self.__domains = domains
		
	def get_domains(self):
		return self.__domains

	def set_dialogue_state(self, dialogue_state_list):
		self.__dialogue_state_list = dialogue_state_list
		
	def get_dialogue_state_list(self):
		return self.__dialogue_state_list
		
	def set_dialogue_acts(self, dialogue_acts_list):
		self.__dialogue_acts_list = dialogue_acts_list
		
	def get_dialogue_acts_list(self):
		return self.__dialogue_acts_list