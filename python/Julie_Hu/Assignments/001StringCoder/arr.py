arr="abcdefghijklmnopqrstuvwxyz"
x= "yes"
	while (x== "yes"):
		string = input('Enter a sentence')
		key =int(input ('Enter a key'))
	for y in range(len(string)):
		index=arr.find(string[y])
		index += key

		newstring.append(arr[index])
print("The original sentence is: "string +"The new sentence is: " + newstring)