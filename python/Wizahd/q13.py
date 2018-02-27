def powArray():
    arr = [1,2,3,4,5]
    for x in range(len(arr)):
        arr[x] = arr[x] ** 2
    print(arr)
powArray()
