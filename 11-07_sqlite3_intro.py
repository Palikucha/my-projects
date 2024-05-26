import sqlite3
import sqlite3

query = """CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT not null,
            email TEXT not null UNIQUE,
            )"""


connection = sqlite3.connect(r"C:\Users\nikol\OneDrive\Desktop\Algebra\Vjezbe\11-07\db_intro.sqlitedoma")

cursor = connection.cursor()

query = """CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT not null,
            email TEXT not null UNIQUE
            )"""


cursor.execute(query)

connection.commit()

connection.close()  