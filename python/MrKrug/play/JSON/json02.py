import json

json1 = '{"wholeThing": {"this":"value1", "that":"value2", "theOther":[1,2,3,4,5]} }'
p01 = json.loads(json1)

for x in p01['wholeThing']:
	if isinstance(p01['wholeThing'][x], list):
		for e in p01['wholeThing'][x]:
			print("==> " + str(e))
	else:
		print(p01['wholeThing'][x])

with open('json02.txt', 'w') as outfile:  
    json.dump(p01, outfile)

