

import sqlite3

conn = sqlite3.connect('Players.db')

cursor = conn.cursor()

query = "update player set plyname = 'Pusarla Venkata Sindhu' where plyid = 'PLY505'"

cursor.execute(query)

conn.commit()
conn.close()