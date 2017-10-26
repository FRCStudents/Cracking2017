
#!/usr/bin/python

###################################################
# In order for this to work... the email must be #
# saved as a text file, then processed...        #
###################################################
import sys
import string

a = []
b = []

with open('EmailIn01', 'r') as fi:
	line = fi.read()
	lines = line.split('\n')
	for l in lines:
		a.append(l)

for x in a:
	if x.find("="):
		b = x.split("=")
		if len(b) > 1:
			print ('name: ' + b[0] + ' and the value: ' + b[1]) 	
