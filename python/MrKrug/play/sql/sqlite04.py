#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print ("opened database successfully")
cursor = conn.execute("UPDATE CRACK SET NAME = 'Hoppalong Cassidy' WHERE ID = 4")
conn.commit()
print ("Table CRACK successfull update")
conn.close()
