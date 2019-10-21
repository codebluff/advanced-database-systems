import sqlite3

con = sqlite3.connect("Database.db")

c = con.cursor()

c.execute("DROP TABLE DMART")
