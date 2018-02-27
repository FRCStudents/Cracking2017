##############################
#
# how do we write comments?
#
##############################

########
# running through the chops...
################################
#
# multiply function
#
def mult(x,y):
	return x * y

#
# add function
# 
################################
def add(x,y):
	return x + y

#
# subtract 
################################
def sub(x,y):
	return x - y

#
# divide
###############################
def div(x,y):
	return x/y 
#
# modulus
###############################
def mod(x,y):
	return x % y
#
# raise x to the power of y
###############################
def pow(x, y):
	return x ** y

def printMenu():
	print("**********************************")
	print("** 1) multiply                  **")
	print("** 2) add                       **")
	print("** 3) divide                    **")
	print("** 4) subtract                  **")
	print("** 5) modulus                   **")
	print("** 6) raise to a power          **")
	print("** 7) end program               **")
	print("**********************************")

#################
# return a choice based on options in the 
# printMenu function
#############################################
def getChoice():
	return input("Make a choice: ")

#################
# get two numbers for the aritmetic operation and
# return as an array of int
#####################################################
def getNumbers():
	x = []
	x += [(int(input("Enter the first number: ")))]
	x += [(int(input("Enter the second number: ")))]
	return x

#################
# run the whole shebang
#####################################################
def runCalculator():
	printMenu()
	c = int(getChoice())
	while(c < 7):
		arr = getNumbers()
		if c == 1:
			print(mult(arr[0], arr[1]))
		if c == 2:
			print(add(arr[0], arr[1]))
		if c == 3:
			print(div(arr[0], arr[1]))
		if c == 4:
			print(sub(arr[0], arr[1]))
		if c == 5:
			print(mod(arr[0], arr[1]))
		if c == 6:
			print(pow(arr[0], arr[1]))
		if c < 7:
			printMenu()
			c = int(getChoice())

#########################
# start the program...
##############################
runCalculator()
