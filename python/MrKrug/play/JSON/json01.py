import json

json1 = '{"this":"value1", "that":"value2"}'
p01 = json.loads(json1)

for elt in p01:
	print(p01[elt])

