print("This is your keyword has to be a string")  
Brutus = input()
print("this is your increment value") 
plus = input()
array1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
array2 = "abcdefghijklmnopqrstuvwxyz"
#x = Brutus.find("y")
#print(x)
print(len(array1[0:5]))
for x in range(len(Brutus)):
    for r in range(0,26):
        if Brutus[x] == array2[r]:
            print(len(array2[0:r+1]))
            a = len(array2[0:r+1])
            b = a + plus
            print(b)
        

