
import glob
import re

######################################################
# doDir2.py                                          #
# This python script does the following:             #
#    	1) Navigates a directory using glob          #
#	2) identifiles all file names ending with    # 
#		.html                                #
#	3) opens and prints those files to terminal  #
######################################################

fromX = ""
fromXSw = False

toX = ""
toXSw = False

dateX = ""
dateXSw = False

parts = []

dict = {}

d = glob.glob("*.txt")
for d2 in d:
	fl = open(d2, "r")
	for line in fl:
		if dateXSw is True:
			dateXSw = False
			dateX = line
		if line[0:7].find("Date:") > -1:
			dateXSw = True

		if toXSw is True:
			toXSw = False
			toX = line
		if line.find("To:") > -1:
			toXSw = True

		if fromXSw is True:
			fromXSw = False
			fromX = line
		if line.find("From:") > -1:
			fromXSw = True

		if line.find("=") > -1:
			parts = line.split("=")
			dict[parts[0]] = parts[1]

	dict['to'] = toX
	dict['from'] = fromX
	dict['date'] = dateX

	for key, item in dict.items():
		print(key + ":\t\t" + item[0:-1])

	print("\n<<<---  t h i s   i s   t h e   e n d   m y   o n l y   f r i e n d  ---->>>")
