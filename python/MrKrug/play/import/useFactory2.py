
import factory2

fList = {} 

def mathSeven():
	global fList
	fList = factory2.makeMath(7)

mathSeven()

print('7 to the third: ' + str(fList['exp'](3)))
print('7 * 21: ' + str(fList['mult'](21)))
print('7 + 18: ' + str(fList['add'](18)))
