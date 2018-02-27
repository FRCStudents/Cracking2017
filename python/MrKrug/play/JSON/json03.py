import json

with open('json02.txt') as json_file:  
    data = json.load(json_file)

print(data)
