
def question01():
	Y = 0
	Y = 17

def question02():
	Y = 17
	Y += 3

def question03():
	myVar = "Thirteen"

def question04():
	myVar = "Thirteen"
	print(myVar[4])

def question05():
	myVar = "Thirteen"
	print(myVar[4:])

def question06():
	myArr = ["Fifteen", "Sixteen", "Seventeen", "Eighteen"]

def question07():
	myArr = ["Fifteen", "Sixteen", "Seventeen", "Eighteen"]
	print(myArr[1])

def question08():
	myArr = ["Fifteen", "Sixteen", "Seventeen", "Eighteen"]
	print(myArr[1:3])

def question09():
	myArr = ["Fifteen", "Sixteen", "Seventeen", "Eighteen"]
	for e in myArr:
		print(e)

def question10():
	myArr = ["Fifteen", "Sixteen", "Seventeen", "Eighteen"]
	myArr.append("Yada")
	for e in myArr:
		print(e)

def question11(myArr):
	myArr.append("Yada")
	for i in range(len(myArr) - 1, -1, -1):
		print(myArr[i])

print("********* question #1 **************")
question01()
print("********* question #2 **************")
question02()
print("********* question #3 **************")
question03()
print("********* question #4 **************")
question04()
print("********* question #5 **************")
question05()
print("********* question #6 **************")
question06()
print("********* question #7 **************")
question07()
print("********* question #8 **************")
question08()
print("********* question #9 **************")
question09()
print("********* question #10 **************")
question10()
print("********* question #11 **************")
myArr = ["Fifteen", "Sixteen", "Seventeen", "Eighteen"]
question11(myArr)
