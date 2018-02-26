
from model import Person

def printStarLine():
	print ('*' * 49)

def printLine(line):
	holdLine = line
	l = len(holdLine)
	while l < 37:
		holdLine = '\t' + holdLine + '\t'
		l += 16
	while l < 48:
		holdLine += '\t'
		l += 8

	holdLine = '*' + holdLine + '*' 
	return holdLine

def showAddView(list):
	printStarLine()
	print(printLine("Enter first name. "))
	print(printLine("Enter last name. "))
	printStarLine()
	print("*>>>>> (name): ")

def showDeleteView(list):
	printStarLine()
	print (printLine("Deleting one of the following: "))
	for item in list:
		print(printLine(item.name()))
	printStarLine()
	print("*>>>>> (name): ")
	
def showAllView(list):
	printStarLine()
	print (printLine('In our database we have ' + str(len(list)) + ' users.'))
	for item in list:
		print (printLine(item.name()))
	printStarLine()

def startView():
	printStarLine()
	print (printLine("MVC - a simple example"))
	print (printLine(" 1) Show everyone in the database."))
	print (printLine(" 2) Delete person from database."))
	print (printLine(" 3) Add person to the database."))
	print (printLine(" e) End program. "))
	printStarLine()


def endView():
	printStarLine()
	print (printLine("Goodbye!"))
	printStarLine()
