from util import *
from MULTIWOZ21_analysis import *
import argparse
import numpy as np

if __name__ == '__main__':
	
	parser = argparse.ArgumentParser()
	parser.add_argument('--data_path', metavar='data_path', required = True, help='data path of MULTIWOZ2.1')
	args = parser.parse_args()
	
	# load total id of dialogs
	basic_path = args.data_path + '/MULTIWOZ2.1/MULTIWOZ2.1'
	data_json_path = basic_path + '/data.json'
	data_json = load_json(data_json_path)
	dialog_id_list = list(set(data_json.keys()))
	# print(dialog_id_list)
	
	# load validate & test id
	valid_list_path = basic_path + '/valListFile.json'
	test_list_path = basic_path + '/testListFile.json'
	
	# get id list of train & validate & test data
	valid_id_list = list(set(load_list_file(valid_list_path)))
	test_id_list = list(set(set(load_list_file(test_list_path))))
	train_id_list = [id for id in dialog_id_list if id not in (valid_id_list + test_id_list)]
	
	print('id of train dialogs:', len(train_id_list))
	print('id of valid dialogs:', len(valid_id_list))
	print('id of test dialogs:', len(test_id_list))
	
	assert(len(dialog_id_list) == len(train_id_list) + len(valid_id_list) + len(test_id_list))
	
	# get train & validate & test data
	train_data, valid_data, test_data = get_train_valid_test_data(data_json, train_id_list, valid_id_list, test_id_list)
	
	assert(len(train_data) == len(train_id_list))
	assert(len(valid_data) == len(valid_id_list))
	assert(len(test_data) == len(test_id_list))
	
	# get multiWOZ data frame list
	multiWOZDataFrameList = []
	
	for i, d in enumerate(train_data):
		assert 'log' in d
		assert 'goal' in d
		
		if i % 500 == 0:
			print('num: ', i)
		
#		print('-' * 50)
#		print()
		
		multiWOZDataFrame = MultiWOZDataFrame()
		
		multiWOZDataFrame.substitute_domain_list(get_domains(d))
		
		multiWOZDataFrame = anlysis_dialogue_log(d, multiWOZDataFrame)
		
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
	
	# save
	np.save('multiWOZDataFrameList', np.array(multiWOZDataFrameList))