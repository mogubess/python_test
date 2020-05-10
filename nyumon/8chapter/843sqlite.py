'''
SQLite
'''
import sqlite3
conn = sqlite3.connect('enterprise.db')
curs = conn.cursor()
#curs.execute('''CREATE TABLE zoo (critter VARCHAR(20) PRIMARY KEY, count INT, damages FLOAT)''')

curs.execute('INSERT INTO zoo VALUES("duck", 5, 0.0)')

a = curs.execute('SELECT * from zoo ORDER BY count')

print(a)

b = curs.fetchall()

print(b)

curs.close()
conn.close()