
import sqlite3

conn = sqlite3.connect('Players.db')

cursor = conn.cursor()

cursor.execute("create database players")

conn.close()
