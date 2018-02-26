#!/usr/bin/python
#conn.execute("INSERT INTO CRACK (ID, NAME, AGE) \
#	VALUES (3, 'Efraim Mordechai', 54)");

import sqlite3
import sys

conn = sqlite3.connect('test.db')
print ("opened database successfully")

try:
	conn.execute("INSERT INTO CRACK (ID, NAME, AGE) VALUES (5, 'BillyBob Jefferies', 17)");

	conn.commit()

except sqlite3.Error as er:
	print ("Error %s: " % er.args[0])
	sys.exit(1)

finally:
	if conn:
		conn.close()
		print ("Connection closed")

print ("Insert routine complete")
