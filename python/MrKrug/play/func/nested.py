
def tester(start):
	def nested(label):
		print(label, state[0])
		state[0] += 1
	state = [start]
	return nested

n = tester(403)
m = n('plusOne')
m = n('plusOneMore')

n('NLabel')
print(m)
