
import factory

fList = []

def mathSeven():
	global fList
	fList = factory.makeMath(7)

mathSeven()

print('7 to the third: ' + str(fList[2](3)))
print('7 * 21: ' + str(fList[0](21)))
print('7 + 18: ' + str(fList[1](18)))
