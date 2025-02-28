
import sqlite3

conn = sqlite3.connect('Players.db')

cursor = conn.cursor()

query = """
create table player (
plyid varchar(5) PRIMARY KEY, 
plyname varchar(50) not null,
sport varchar(30) not null, 
acheivement varchar(50) not null
)
"""

cursor.execute(query)

conn.close()