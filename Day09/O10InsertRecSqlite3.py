
import sqlite3

conn = sqlite3.connect('Players.db')

cursor = conn.cursor()

FL = open("query.txt", "r")

for line in FL.readlines():
    cursor.execute(line)

conn.commit()
conn.close()
FL.close()
