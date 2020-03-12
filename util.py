import json

# load json
def load_json(path):
	with open(path) as json_file:
		return json.load(json_file)

# load list file
def load_list_file(path):
	with open(path, 'r') as file:
		dialog_id_list = file.readlines()
		dialog_id_list = [l.strip('\n') for l in dialog_id_list]
		return dialog_id_list

# get train & validate & test data
def get_train_valid_test_data(data_json, train_id_list, valid_id_list, test_id_list):
	train_data = [v for k, v in data_json.items() if k in train_id_list]
	valid_data = [v for k, v in data_json.items() if k in valid_id_list]
	test_data = [v for k, v in data_json.items() if k in test_id_list]
	return train_data, valid_data, test_data