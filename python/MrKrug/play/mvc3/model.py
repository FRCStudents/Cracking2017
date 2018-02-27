import sqlite3 

class People(object):
	def __init__(self):
		self.peopleArray = []
		self.dbName = "mcv3.db"
		self.loadArray()	

	def getPeople(self):
		self.loadArray()
		return self.peopleArray

	def getAll(self):
		return self.getPeople()

	def getPerson(self, idx):
		for p in self.peopleArray:
			if p.id == idx:
				return p
		return None

	def deletePerson(self, idx):
		conn = sqlite3.connect(self.dbName)
		sql = "DELETE FROM PERSONS WHERE rowid=" + str(idx)
		cursor = conn.execute(sql)
		conn.commit()
		conn.close()
		self.loadArray()

	def addPerson(self, first_name, last_name):
		conn = sqlite3.connect(self.dbName)
		str = "INSERT INTO PERSONS (FIRST_NAME, LAST_NAME) VALUES ('" + first_name + "', '" + last_name + "')"	
		conn.execute(str);
		conn.commit()
		self.loadArray()

	def loadArray(self):
		self.peopleArray = []
		conn = sqlite3.connect(self.dbName)

		cursor = conn.execute("SELECT rowid, FIRST_NAME, LAST_NAME FROM PERSONS")
		for row in cursor:
			person = Person(row[0], row[1], row[2])
			self.peopleArray.append(person)

		conn.close()


class Person(object):
	def __init__(self, id=None, first_name= None, last_name = None):
		self.id = id
		self.first_name = first_name
		self.last_name = last_name

	def name(self):
		return ("[%d] %s %s" % (self.id, self.first_name, self.last_name))


if __name__ == "__main__":
	pepl = People()
	p = Person()
