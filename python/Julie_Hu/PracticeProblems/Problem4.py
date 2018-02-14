def occurance():
    a = 0
    arr = [1,1,1,2,4,5]
    for x in range(len(arr)):
        for y in range(x - 1):
            if arr[x] == arr[y + 2]:
                a += 1
    print(a)
occurance()