#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print ("opened database successfully")
cursor = conn.execute("DELETE FROM CRACK WHERE ID=1")
conn.commit()
print ("Table CRACK successfull update")
conn.close()
