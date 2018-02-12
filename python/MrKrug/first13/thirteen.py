
def powArray(arr, exp):
	for i in range(len(arr)):
		arr[i] **= exp
		arr[i] = round(arr[i]) 

a = [2,4,6,8,10,12,14,16,18,20]
print(a)
powArray(a, 3)
print(a)

powArray(a, 1/3)
print(a)
