arr="abcdefghijklmnopqrstuvwxyz"
x= "yes"
newstring=[]
while (x== "yes"):
    string = input('Enter a sentence')
    key =int(input ('Enter a key'))
    for y in range(len(string)):
        index=arr.find(string[y])
        index += key
        if (index >25):
            index-=25
    newstring.append(arr[index])
print("The new sentence is: " + newstring)

