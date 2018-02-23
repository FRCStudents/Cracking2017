
class myClass:
	def __init__(self, start):
		self.state = start

	def getState(self):
		return self.state

	def setState(self, x):
		self.state = x

	def getFirst(self):
		return self.state[0]

mC = myClass(['this','that'])
print(mC.getFirst())
