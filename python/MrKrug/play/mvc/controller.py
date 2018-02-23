
from model import Person
import view

def showAll():
	peep = Person()
	peopleArray = peep.getAll()
	return view.showAllView(peopleArray)

def start():
	view.startView()
	data_in = input()
	if data_in == 'y':
		return showAll()
	else:
		return view.endView()

if __name__ == "__main__":
	start()
