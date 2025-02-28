
import sqlite3

import flask.cli
from prettytable import from_db_cursor

conn = sqlite3.connect('Players.db')

cursor = conn.cursor()

cursor.execute("select * from player")

FW = open("Players.txt", "w")

# for row in cursor.fetchall():
#     FW.write(str(row)+ "\n")



prtyTbl = from_db_cursor(cursor)

FW.write(str(prtyTbl))

FW.close()

# print(prtyTbl)
# FW.close()
conn.close()

