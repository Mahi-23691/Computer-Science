import sqlite3

db = sqlite3.connect("SQL\Phones\phones.db")

cursor = db.cursor()
sql = 'SELECT * FROM phones;'
cursor.execute(sql)

results = cursor.fetchall()
print(results)

db.close()