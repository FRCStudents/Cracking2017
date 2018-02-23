#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print ("opened database successfully")
cursor = conn.execute("SELECT ID, NAME, AGE FROM CRACK")

for row in cursor:
	print ("ID = ", row[0], "NAME = ", row[1], "AGE = ", row[2])

print ("Table CRACK successfull select")
conn.close()
