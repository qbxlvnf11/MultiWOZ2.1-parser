from MULTIWOZ21_frame import *

# extract domains from MULTIWOZ2.1
def get_domains(d):
	
	domains = []
	ignore_keys_in_goal = ['message', 'topic']
	for dom_k, dom_v in d['goal'].items():
		if dom_v and dom_k not in ignore_keys_in_goal:
			domains.append(dom_k)
	
	return domains

# extract messages from MULTIWOZ2.1
def get_messages(d):
	
	messages = d['goal']['message']
	
	return messages

# extract user dialogue, system dialogue, dialogue state from MULTIWOZ2.1
def anlysis_dialogue_log(d, multiWOZDataFrame):
	
	for i, t in enumerate(d['log']):
		if i % 2 != 0: # System
			multiWOZDataFrame.append_dialogue('Sys: ' + t['text'])
			dialogueState = DialogueState(t['metadata'])
			multiWOZDataFrame.append_dialogue_state(dialogueState)
		else: # User
			multiWOZDataFrame.append_dialogue('User: ' + t['text'])
			
	return multiWOZDataFrame

# extract user dialogue, system dialogue, dialogue state from MULTIWOZ2.1
def anlysis_dialogue_acts(k, acts_json, multiWOZDataFrame):
	
	for k, acts in acts_json[k[:-5]].items():
		multiWOZDataFrame.append_dialogue_acts(acts)
	
	return multiWOZDataFrame

# get multiWOZ data frame list
def get_multiWOZ_data_frame_list(data_list, key_list, acts_json):
	
	multiWOZDataFrameList = []
	
	for i in range(len(data_list)):
		assert 'log' in data_list[i]
		assert 'goal' in data_list[i]
		
		if i % 500 == 0:
			print('num: ', i)
		
#		print('-' * 50)
#		print()
		
		multiWOZDataFrame = MultiWOZDataFrame()
		
		multiWOZDataFrame.substitute_domain_list(get_domains(data_list[i]))
		
		multiWOZDataFrame = anlysis_dialogue_acts(key_list[i], acts_json, multiWOZDataFrame)
		
		multiWOZDataFrame = anlysis_dialogue_log(data_list[i], multiWOZDataFrame)
		
		multiWOZDataFrameList.append(multiWOZDataFrame)
		
#		print('domain', multiWOZDataFrame.get_domain_list())
#		for i in range(len(multiWOZDataFrame.get_dialogue_state_list())):
#			print('num: ', i + 1)
#			print('taxi_bool: ', multiWOZDataFrame.get_dialogue_state_list()[i].taxi_bool)
#			print('police_bool: ', multiWOZDataFrame.get_dialogue_state_list()[i].police_bool)
#			print('restaurant_bool: ', multiWOZDataFrame.get_dialogue_state_list()[i].restaurant_bool)
#			print('bus_bool: ', multiWOZDataFrame.get_dialogue_state_list()[i].bus_bool)
#			print('hospital_bool: ', multiWOZDataFrame.get_dialogue_state_list()[i].hospital_bool)
#			print('hotel_bool: ', multiWOZDataFrame.get_dialogue_state_list()[i].hotel_bool)
#			print('hotel_hotel_semi_name: ', multiWOZDataFrame.get_dialogue_state_list()[i].hotel_semi_name)
#			print('attraction_bool: ', multiWOZDataFrame.get_dialogue_state_list()[i].attraction_bool)
#			print('train_bool: ', multiWOZDataFrame.get_dialogue_state_list()[i].train_bool)
#			print()
	
	return multiWOZDataFrameList