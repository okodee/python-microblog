import sqlite3

connection = sqlite3.connect('database.db')

cur = connection.cursor()

query = "ALTER TABLE user ADD EMAIL VARCHAR (255)"

cur.execute(query)

connection.commit()

connection.close()