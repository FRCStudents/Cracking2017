import time

###################################################
# This is a loop - range is 0, 1, ... 49
# therefore: the line means:
#            Do the following commands 50 times
#            First i = 0
#            Next i = 1
#            and so on, until i = 49
################################################## 
for i in range(50):
	time.sleep(1)
	j = i + 1
	y = ord('!') + i 
	c = chr(y)
	print(j * c + "\r")

