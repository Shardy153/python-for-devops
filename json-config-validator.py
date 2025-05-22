### JSON Config Validator

#Problem: Load a JSON config and ensure required keys like `"service"`, `"port"`, `"env"` exist. Return missing keys.
#Skills: JSON handling, Dict operations, Validation

import json

def validate(json_object):
	keys =  json_object.keys()
	result = []
	expected_keys = ["service", "port", "env"]
	for expected_key in expected_keys:
		if expected_key not in keys:
			result.append(expected_key)
	return "missing keys : " + str(result)
			
file_path = "json.config"
with open(file_path, 'r') as file:
    json_object = json.load(file)
print(validate(json_object))
