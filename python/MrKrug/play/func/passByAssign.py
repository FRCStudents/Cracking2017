
def changeIt(x):
	x = 13 
	print("Inside: this is y: " + str(x))

def enclosing():
	enc01 = 13
	def enclosed():
		nonlocal enc01
		enc01 += 1
		print('nonlocal: ' + str(enc01))
	enclosed()
	print(enc01)
enclosing()

y = 5
print("This is y: " + str(y))
changeIt(y)
changeIt.attr = 15
print("Just for fun: " + str(changeIt.attr))
print("Now, this is y: " + str(y))  
