
#
# This is a birthday tracker for some set of
# people - and a small piece of i/o. We will
# list the poeple for the user, and the user
# will choose a person and we will display
# their birthday... and that's it! 
#

class box:
	def __init__(self, birthday, fname, lname):
		self.birthday = birthday
		self.fname = fname
		self.lname = lname

	def getBirthday(self):
		return self.birthday

	def getFName(self):
		return self.fname

	def getLName(self):
		return self.lname	

	def setLName(self, lname):
		self.lname = lname

	def setFName(self, fname):
		self.fname = fname

	def setBirthday(self, bday):
		self.birthday = bday

birthdayBox = []
names = [{'fname':'Joey', 'lname':'Uberman', 'birthday':'03/30/58'},
{'fname':'Madge', 'lname':'Hinterspall', 'birthday':'05/19/72'},
{'fname':'Irving', 'lname':'Dagall', 'birthday':'09/12/1924'}]

def fillData():
	for i in range(3):
		fname = input("Enter first name: (enter for default) ")
		if len(fname) < 3:
			fname = names[i]['fname']
			lname = names[i]['lname']
			birthday = names[i]['birthday']
		else:
			lname = input("Enter last name: ")
			birthday = input("Enter birthday: ")

		b = box(birthday, fname, lname)
		birthdayBox.append(b)

def showData():
	for i in range(len(birthdayBox)):
		print("Person: " + birthdayBox[i].fname + " " + birthdayBox[i].lname)

def getName():
	name = input("Enter the name you want to lookup: ")
	n = name.split(' ')
	return getBirthday(n)

def getBirthday(name):
	if(len(name)) < 2:
		fname = name[0]
	else:
		fname = name[0]
		lname = name[1]

	found = False
	for n in birthdayBox:
		if n.fname == fname:
			return n.birthday
	for n in birthdayBox:
		if n.lname == lname:
			return n.birthday

		
fillData()
showData()		
print(getName())


