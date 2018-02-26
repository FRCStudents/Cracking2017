import json

class People(object):
	def __init__(self):
		self.peopleArray = []
		self.getAll()

	def getPeople(self):
		return self.peopleArray

	def getPerson(self, idx):
		return self.peopleArray[idx]

	def deletePerson(self, idx):
		del self.peopleArray[idx]

	def addPerson(self, first_name, last_name):
		p = Person(first_name, last_name)
		self.peopleArray.append(p)

	def saveAll(self):
		product = {"items":[]}
		for elt in self.peopleArray:
			dict = {"item": {"first_name":"", "last_name":""}}
			dict["item"]["first_name"] = elt.getFirst()
			dict["item"]["last_name"] = elt.getLast()
			product["items"].append(dict)
		with open('db2.txt', 'w') as outfile:  
    			json.dump(product, outfile)


	def getAll(self):
		database = open('db2.txt', 'r')
		result = []
		jlist = json.loads(database.read())
		for item in jlist:
			for item2 in jlist[item]:
				person = Person(item2['item']['first_name'], item2['item']['last_name'])
				result.append(person)

		self.peopleArray = result
		return result



class Person(object):
	def __init__(self, first_name= None, last_name = None):
		self.first_name = first_name
		self.last_name = last_name

	def getFirst(self):
		return self.first_name

	def getLast(self):
		return self.last_name

	def name(self):
		return ("%s %s" % (self.first_name, self.last_name))


if __name__ == "__main__":
	pepl = People()
	p = Person()
