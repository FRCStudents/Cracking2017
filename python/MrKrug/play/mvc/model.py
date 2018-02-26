import json

class Person(object):
	def __init__(self, first_name= None, last_name = None):
		self.first_name = first_name
		self.last_name = last_name

	def name(self):
		return ("%s %s" % (self.first_name, self.last_name))

	def getAll(self):
		database = open('db2.txt', 'r')
		result = []
		jlist = json.loads(database.read())
		for item in jlist:
			for item2 in jlist[item]:
				person = Person(item2['item']['first_name'], item2['item']['last_name'])
				result.append(person)
		return result


