
f = open('in.file', 'r')
data = f.read()
arr = data.splitlines()
f.seek(27)
data = f.read(15)
print("15 char @ 27: ", data)
f.close()
for l in arr:
	print('array entry: ', l)
