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