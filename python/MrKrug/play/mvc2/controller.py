
from model import People, Person
import view

people = None

def initDB():
	global people 
	people = People()
	peopleArray = people.getAll()

def showAll():
	peopleArray = people.getPeople()
	return view.showAllView(peopleArray)

def addUser():
	peopleArray = people.getPeople()
	view.showAddView(peopleArray)
	fName = input("Enter first name: ")
	lName = input("Enter last name: ")
	p = Person(fName, lName)
	peopleArray.append(p)

def deleteUser():
	peopleArray = people.getPeople()
	view.showDeleteView(peopleArray)
	data_in = input()
	idx = 0
	pos = 0
	for p in peopleArray:
		if data_in == p.first_name:
			pos = idx
		idx += 1
	del peopleArray[pos]
	return view.showAllView(peopleArray)

def handleMenu(choice):
	if choice == '1':
		return showAll()
	if choice == '2':
		return deleteUser()
	if choice == '3':
		return addUser()

def start():
	initDB()
	view.startView()
	data_in = input()
	while data_in != 'e':
		handleMenu(data_in)
		view.startView()
		data_in = input()	
	people.saveAll()
	return view.endView()

if __name__ == "__main__":
	start()
