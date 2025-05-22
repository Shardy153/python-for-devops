import yaml
import json

yaml_file_name = "hpa.yaml"
json_file_name = "hpa.json"
with open(yaml_file_name, 'r') as f:
    data = yaml.load(f, Loader=yaml.SafeLoader)
    
# Print the values as a dictionary
print(data)


with open(json_file_name, "w") as json_file:
    json.dump(data, json_file, indent=4)
