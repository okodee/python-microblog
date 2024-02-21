import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    sqlStatment = f.read()
    connection.executescript(sqlStatment)

cur = connection.cursor()

cur.execute(quit)

connection.commit()

connection.close()