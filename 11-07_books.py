# aplikacija za praćenje knjiga u knjižari.

# aplikacija pradi knjige i njihove autore.
# o autorima znamo ime i prezime, a o knjigama naslov, cijenu, dostupnost (je/nije) i autora.

# u tu svrhu, potrebno je kreirati 2 tablice, jednu koja će spremati podatke o autorima, a drugu koja će spremati podatke o knjigama.
# obje tablice će imati i podatak o ID-u kojeg će koristiti kao primarni ključ.

# relacija autor-knjiga će biti one-to-many, s obzirom da će svaka knjiga imati točno jednog autora, a pojedini autor može biti autor više knjigaimport sqlite3


import sqlite3


connection = sqlite3.connect('bookstore.db')

cursor = connection.cursor()

# napravi tablicu za autore
create_table_author_query = '''CREATE TABLE IF NOT EXISTS author (
    id INTEGER PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    surname VARCHAR(30) NOT NULL
);'''

create_table_book_query = '''CREATE TABLE IF NOT EXISTS book (
    id INTEGER PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    price FLOAT NOT NULL,
    is_available BOOL NOT NULL,
    author_id INTEGER NOT NULL
);'''

def get_connection(db_name):
    try: 
        connection = sqlite3.connect(db_name)
        return connection
    except sqlite3.Error as err:
        print("error: {err}")


class Author:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

class Book:
    def __init__(self, id, title, price, available, author):
        self.id = id
        self.title = title
        self.price = price
        self.available = available
        self.author = author  # This should be an instance of the Author class

def create_db_table(connection, create_table_query):
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        connection.commit()
        print("Table created successfully")
    except sqlite3.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor != None:
            cursor.close()

def save_author(connection, author):
    try:
        cursor = connection.cursor()
        cursor.execute(f'''
            INSERT INTO authors (first_name, last_name)
            VALUES ('{author.first_name}', '{author.last_name}')
        ''')
        connection.commit()
        print("Author saved successfully")
    except sqlite3.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor != None:
            cursor.close()



def main():
    db_connection = get_connection('Vjezbe\11-07\db_intro.sqlitedoma')

if __name__ == "__main__":
    main()
