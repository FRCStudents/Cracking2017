
import glob
import re

######################################################
# doDir.py                                           #
# This python script does the following:             #
#    	1) Navigates a directory using glob          #
#	2) identifiles all file names ending with    # 
#		.html                                #
#	3) opens and prints those files to terminal  #
######################################################
d = glob.glob("*")
for d2 in d:
	e = glob.glob(d2 + "/*")
	print("Directory: " + d2)
	for e2 in e:
		if e2.find("html") > -1:
			print ("\t File '" + e2 + "' ==>" )
			fl = open(e2, 'r')
			num = 1
			for line in fl:
				wierdCharCount = len(re.findall("\W", line))
				print ("(line [" + str(num) + "][" + str(wierdCharCount - 1) + "])==> " + line)
				num += 1	
