#!/usr/bin/python

import sys
import string

a = []
b = []

with open('EmailSave', 'r') as fi:
	line = fi.read()
	lines = line.split('\n')
	for l in lines:
		a.append(l)

for x in a:
	if x.find("="):
		b = x.split("=")
		if len(b) > 1:
			print ('name: ' + b[0] + ' and the value: ' + b[1]) 	
