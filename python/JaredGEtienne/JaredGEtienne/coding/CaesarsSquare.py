print("This is your keyword has to be a string")  
Brutus = input()
print("this is your increment value") 
plus = input()
array1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
array2 = "abcdefghijklmnopqrstuvwxyz"
#x = Brutus.find("y")
#print(x)
b = []
for x in range(len(Brutus)):
    for r in range(0,25):
        if Brutus[x] == array2[r]:
            a = len(array2[0:r+1])
            b.append(len(array2[0:r+1]) + int(plus))
    if Brutus[x] == array2[25]:
        b.append(int(plus) - 1)
print("this is the value of the array increased")
print(b)
print("this is the conversion")
print(b)
print(Brutus)
print("this is array increased")
for y in range(len(b)):
    for z in range(0,25):
        if b[y] == len(array2[0:z+1]):
            b[y] = array2[z]
print(b)
