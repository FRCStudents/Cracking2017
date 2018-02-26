
def makeMath(NumberIn):
	def mult(newNum):
		return NumberIn * newNum

	def add(newNum):
		return NumberIn + newNum

	def exp(newNum):
		return NumberIn ** newNum

	return {'mult': mult, 'add': add, 'exp':exp}
