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

# get train & validate & test data, key
def get_train_valid_test_data(data_json, train_id_list, valid_id_list, test_id_list):
	train_data = []
	train_key = []
	valid_data = []
	valid_key = []
	test_data = []
	test_key = []
	
	for k, v in data_json.items():
		if k in train_id_list:
			train_key.append(k)
			train_data.append(v)
	
		if k in valid_id_list:
			valid_key.append(k)
			valid_data.append(v)
	
		if k in test_id_list:
			test_key.append(k)
			test_data.append(v)
	
	return train_data, train_key, valid_data, valid_key, test_data, test_key