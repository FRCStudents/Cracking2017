import random

maximummistakes = 10

WORDS = ("python", "javascript","code","cracking","answer", "hangman")
word = random.choice(WORDS)

def getWord():
	word = WORDS[random.randint(0, len(WORDS) - 1)]
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
		print("You are a WINNER!")
		return True

	print(showWord)
	return False

word = getWord()
while showWord() != True:
	x = input("What letter do you want to guess? ")
	if (isInWord(x)):
		letterUsed(x)
	else:
		numberMissed += 1
		print("That's not correct: " + str(numberMissed) + " mistakes!")
		if numberMissed > maximummistakes:
			print("You Lose!")
			exit()
