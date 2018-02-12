import random

MAX_MISTAKES = 10

words = ['this', 'that', 'happy', 'fairly', 'fantastic', 'completely', 'really', 'awesome']
word = ""
used = ""
numberMissed = 0

def getWord():
	word = words[random.randint(0, len(words) - 1)]
	return word

def isInWord(c):
	if(word.find(c) > -1):
		return True

	return False

def letterUsed(c):
	global used
	used += c

def letterInUsed(c):
	if(used.find(c) > -1):
		return True
	return False

def showWord():
	showWord = ""
	for c in word:
		if(letterInUsed(c)):
			showWord += c
		else:
			showWord += ' _'
	if(showWord == word):
		print("You have won this game!")
		return True

	print(showWord)
	return False

word = getWord()
while showWord() != True:
	#print(word)
	x = input("Enter a letter: ")
	if (isInWord(x)):
		letterUsed(x)
	else:
		numberMissed += 1
		print("That's bad: " + str(numberMissed) + " mistakes!")
		if numberMissed > MAX_MISTAKES:
			print("You Lose!")
			exit()
