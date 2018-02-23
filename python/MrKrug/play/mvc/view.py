
from model import Person

def showAllView(list):
	print ('In our database we have ' + str(len(list)) + ' users. Here they are: ')

	for item in list:
		print (item.name())

def startView():
	print ("MVC - a simple example")
	print ("Show everyone in the database? (y/n): ")

def endView():
	print ("Goodbye!")
