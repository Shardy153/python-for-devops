# **Problem**: Convert a CSV file of users or services into a JSON list of dictionaries.
# **Skills**: `csv`, `json`, File Manipulation

import csv
import json
def csv_to_json(file_name):
	result = []
	with open(file_name, "r") as file:
		csv_file =  csv.DictReader(file)
		for line in csv_file:
			result.append(line)
	
	with open("mydata.json", "w") as final:
		json.dump(result, final)

csv_to_json("test.csv")			
