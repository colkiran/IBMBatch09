
import sqlite3

conn = sqlite3.connect('Players.db')

cursor = conn.cursor()

query = "delete from player where plyid = 'PLY323'"

cursor.execute(query)

conn.commit()
conn.close()