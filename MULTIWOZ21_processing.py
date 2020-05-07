import operator
from MULTIWOZ21_frame import *

# extract global dialogue state slot set from MULTIWOZ2.1 data.json
def build_dialogue_state_slot_set(data_json):
	
	dialogue_state_slot_set = set()
	
	for id, d in data_json.items():
		for i, t in enumerate(d['log']):
			if i % 2 == 1:
				for domain, sub in t['metadata'].items():
					for slot in sub['book']:
						dialogue_state_slot_set.add(domain + ' ' + 'book' + ' ' + slot)
                        
					for slot in sub['semi']:
						dialogue_state_slot_set.add(domain + ' ' + 'semi' + ' ' + slot)

	print('-' * 20, 'dialogue_state_slot_set', '-' * 20)
	print('length of dialogue_state_slot_set:', len(dialogue_state_slot_set))   
    
	dialogue_state_slot_list = list(dialogue_state_slot_set)
	dialogue_state_slot_list.sort()
	for slot in dialogue_state_slot_list:
		print(slot)
    
	return dialogue_state_slot_set

# extract global ontology dictionalry (slot-value) from MULTIWOZ2.1 ontology.json
def build_ontology_dic(ontology_json):
	
	ontology_slot_value_dic = {}
	
	for k, v in ontology_json.items():
		k_split = k.split('-')
		domain = k_split[0]
		k_split_split = k_split[1].split(' ')
        
		if len(k_split_split) == 1:
			k = domain + ' semi ' + k_split_split[0]
		elif len(k_split_split) == 2:
			if k_split_split[0] == 'book':
				k = domain + ' book ' + k_split_split[1]
			else:
				if k_split_split[1] == 'range':
					k = domain + ' book ' + k_split_split[0] + k_split_split[1]
				else:
					k = domain + ' book ' + k_split_split[0] + k_split_split[1].capitalize()            

		ontology_slot_value_dic[k] = v

	print('-' * 20, 'ontology_slot_list', '-' * 20)
	print('length of ontology_slot_set:', len(ontology_slot_value_dic.keys()))

	ontology_slot_list = list(ontology_slot_value_dic.keys())
	ontology_slot_list.sort()

	for slot in ontology_slot_list:
		print(slot)

	return ontology_slot_value_dic

# extract domain information from MULTIWOZ2.1 data.json
def extract_domain(d):
	
	domains = []
	ignore_keys_in_goal = ['message', 'topic']
	for dom_k, dom_v in d['goal'].items():
		if dom_v and dom_k not in ignore_keys_in_goal:
			domains.append(dom_k)
	
	return domains

# extract message information from MULTIWOZ2.1 data.json
def extract_message(d):
	
	messages = d['goal']['message']
	
	return messages

# extract user dialogue, system dialogue, dialogue state from MULTIWOZ2.1 data.json
def extract_dialogue_state(d, ontology_slot_value_dic):
	dialogue_state_list = []
    
	for i, t in enumerate(d['log']):
		dialogue_state_list.append(DialogueState(t, ontology_slot_value_dic))
			
	return dialogue_state_list

# extract dialogue acts information from MULTIWOZ2.1 dialogue_acts.json
def extract_dialogue_acts(k, acts_json):
	
	act_list = []
	sorted_key = sorted(acts_json[k[:-5]].items(), key=operator.itemgetter(0))
	
	for k, acts in sorted_key:
		act_list.append(acts)
	
	return act_list

# get multiWOZ data frame list
def get_multiWOZ_data_frame_list(data_list, key_list, acts_json, ontology_slot_value_dic):
	
	multiWOZDataFrameList = []
	
	for i in range(len(data_list)):
		assert 'log' in data_list[i]
		assert 'goal' in data_list[i]
		
		multiWOZDataFrame = MultiWOZDataFrame(key_list[i])
		
		multiWOZDataFrame.set_domains(extract_domain(data_list[i]))
		
		multiWOZDataFrame.set_dialogue_state(extract_dialogue_state(data_list[i], ontology_slot_value_dic))
		
		multiWOZDataFrame.set_dialogue_acts(extract_dialogue_acts(key_list[i], acts_json))
		
		multiWOZDataFrameList.append(multiWOZDataFrame)
        
		if i % 500 == 0:
			print('-' * 50)
			print('- example number:', (i + 1))
			print()
			print('- id:', multiWOZDataFrame.id) 
			print()            
			print('- domain:', multiWOZDataFrame.get_domains())
			print()
			for dialogue_state in multiWOZDataFrame.get_dialogue_state_list():
				print()
				print('-- dialogue:', dialogue_state.get_dialogue())
				print()
				if dialogue_state.dialogue_state_flag:
					print('-- slot_value_dic')
					for k, v in dialogue_state.get_slot_value_dic().items():
						print('---', k)
						print(v)
					print()
					print('-- label_dic')
					for k, v in dialogue_state.get_label_dic().items():
						print('---', k)
						print(v)
					print()
			print('- dialogue_acts')
			for dialogue_acts in multiWOZDataFrame.get_dialogue_acts_list():
				print(dialogue_acts)
			print('-' * 50)
			
	return multiWOZDataFrameList