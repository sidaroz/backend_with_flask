import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (username, email) VALUES (?, ?)",
            ('jaxsan', 'jaxsan@gmail.com')
            )

cur.execute("INSERT INTO users (username, email) VALUES (?, ?)",
            ('nowshad', 'nowshad@gmail.com')
            )

cur.execute("INSERT INTO users (username, email) VALUES (?, ?)",
            ('sami', 'sami@gmail.com')
            )

connection.commit()
connection.close()