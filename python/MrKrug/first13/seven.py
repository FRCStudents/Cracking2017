
arr = [5,10,15,20,25]
arr.append(30)

arrSpecified = ['this', 'that']
for m in arrSpecified:
	arr.append(m)

newItem = 'New Item'
arr[1:1] = [newItem]

print(len(arr))
print(arr)

del arr[2]
print('took out index: 3')
print(arr)
