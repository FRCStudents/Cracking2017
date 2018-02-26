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

def deleteUser():
	peopleArray = people.getPeople()
	view.showDeleteView(peopleArray)
	data_in = input()
	pos = 0
	for p in peopleArray:
		if data_in == p.first_name:
			pos = p.id 
	#del peopleArray[pos]
	people.deletePerson(pos)
	return view.showAllView(peopleArray)

def addUser():
	peopleArray = people.getPeople()
	view.showAddView(peopleArray)
	first_name = input()
	last_name  = input()
	people.addPerson(first_name, last_name)

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
	return view.endView()

if __name__ == "__main__":
	start()
