
def printBack(arr):
	for i in range(len(arr)-1, -1, -1):
		print(arr[i])

arr2 = [5,10,15,20,25]
arr2.append(30)
printBack(arr2)
