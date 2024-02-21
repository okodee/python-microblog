import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    sqlStatement = f.read()
    connection.executescript(sqlStatement)


cur = connection.cursor()

cur.execute('Insert into user (username, password) values (?,?)', ('oo1','password'))

cur.execute('Insert into user (username, password) values (?,?)', ('ob2','password2'))


connection.commit()

connection.close()