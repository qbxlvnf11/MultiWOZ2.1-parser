from util import *
from MULTIWOZ21_analysis import *
import argparse
import numpy as np

if __name__ == '__main__':
	
	parser = argparse.ArgumentParser()
	parser.add_argument('--load_data_path', metavar='load_data_path', required = True, help='data load path of MULTIWOZ2.1')
	parser.add_argument('--save_data_path', metavar='save_data_path', required = True, help='data save path of MULTIWOZ2.1')
	args = parser.parse_args()
	
	# load data json and acts json, total id of dialogs
	basic_path = args.load_data_path + '/MULTIWOZ2.1/MULTIWOZ2.1'
	data_json_path = basic_path + '/data.json'
	data_json = load_json(data_json_path)
	acts_json_path = basic_path + '/dialogue_acts.json'
	acts_json = load_json(acts_json_path)
	dialog_id_list = list(set(data_json.keys()))
	
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
	train_data, train_key, valid_data, valid_key, test_data, test_key = get_train_valid_test_data(data_json, train_id_list, valid_id_list, test_id_list)
	
	assert(len(train_data) == len(train_id_list))
	assert(len(valid_data) == len(valid_id_list))
	assert(len(test_data) == len(test_id_list))
	
	# get multiWOZ train data frame list
	multiWOZDataFrameListTrain = get_multiWOZ_data_frame_list(train_data, train_key, acts_json)
	print('train data')
	multiWOZDataFrameListValid = get_multiWOZ_data_frame_list(valid_data, valid_key, acts_json)
	print('valid data')
	multiWOZDataFrameListTest = get_multiWOZ_data_frame_list(test_data, test_key, acts_json)
	print('test data')
	
	# save
	np.save(args.save_data_path + '/multiWOZDataFrameListTrain', np.array(multiWOZDataFrameListTrain))
	np.save(args.save_data_path + '/multiWOZDataFrameListValid', np.array(multiWOZDataFrameListValid))
	np.save(args.save_data_path + '/multiWOZDataFrameListTest', np.array(multiWOZDataFrameListTest))