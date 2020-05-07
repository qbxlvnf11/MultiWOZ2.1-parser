class DialogueState:
	def __init__(self, t, ontology_slot_value_dic):
		self.__dialogue = t['text']
		self.dialogue_state_flag = False
		
		if str(t['metadata']) != '{}':
			self.dialogue_state_flag = True
			self.__slot_value_dic = {}
			self.__label_dic = {}
			self.__build_slot_value_dic(ontology_slot_value_dic, t['metadata'])
        
	def __build_slot_value_dic(self, ontology_slot_value_dic, metadata):
		for slot in ontology_slot_value_dic.keys():
			slot_split = slot.split(' ')
			try:
				if metadata[slot_split[0]][slot_split[1]][slot_split[2]] != 'not mentioned' and metadata[slot_split[0]][slot_split[1]][slot_split[2]] != '':
					self.__slot_value_dic[slot] = ontology_slot_value_dic[slot]
					self.__label_dic[slot] = metadata[slot_split[0]][slot_split[1]][slot_split[2]]
			except Exception as e: None
		
	def get_dialogue(self):
		return self.__dialogue
        
	def get_slot_value_dic(self):
		return self.__slot_value_dic
        
	def get_label_dic(self):
		return self.__label_dic