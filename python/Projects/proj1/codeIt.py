
arr = "abcdefghijklmnopqrstuvwxyz"
newSentence = []

response = "yes"

while(response == "yes"):
	newSentence = []
	print("Enter a sentence to code: ")
	sentence = input()
	print("Enter a key: ")
	key = int(input())
	for i in range(len(sentence)):
		idx = arr.find(sentence[i].lower())
		idx += key
		if(idx > 25):
			idx -= 25
		newSentence.append(arr[idx])
	print("Go again?")
	print(''.join(newSentence))
	print("Go again? ('no'): ")
	response = input()
