#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('mcv3.db')
print ("opened database successfully")
conn.execute('''DROP TABLE PERSONS;''')
conn.execute('''CREATE TABLE PERSONS 
		(FIRST_NAME TEXT NOT NULL,
		LAST_NAME  TEXT NOT NULL);''')

print ("Table Persons successfully created")
conn.close()
