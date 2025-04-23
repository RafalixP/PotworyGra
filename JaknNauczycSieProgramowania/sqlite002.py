'''
1.Utworzyć tabelę, dwie kolumny: name, lastname
2.Dodać po kolei trzy rekord
3. Wyświetlić tabelę
4.Usunąć jeden wiersz/trzy wiersze
5. Wyświetlić tabelę
'''
import sqlite3

connection = sqlite3.connect('sqlite_baza002.db')
cur = connection.cursor()

names_list = [
    ('Rafal', 'Pieczka'),
    ('Isaac', 'Newton'),
    ('Abraham', 'Lincoln')
]

def create_table(connection):
    cur.execute('''CREATE TABLE IF NOT EXISTS people (name text, lastname text)''')
    connection.commit()

def show_table(connection):

     cur.execute('''SELECT * FROM people''')
     table = cur.fetchall()

     for row in table:
        print(str(row[0]) + ' - ' + row[1])

def add_records(connection):

    cur.executemany('''INSERT INTO 'people' (name, lastname) VALUES (?,?)''', names_list)
    connection.commit()

def delete_records(connection):
    cur.execute(''' DELETE FROM people WHERE 1 = 1 ''')
    connection.commit()


create_table(connection)
print('Pusta tabela utworzona, oto jej zawartość: ')
print()
show_table(connection)
print('Dodajemy rekordy...')
print()
add_records(connection)
print('Poniżej tabela zawierająca jakieś dane:')
print()
show_table(connection)
print()
delete_records(connection)                    
print()
print('Poniżej tabela z której usuneliśmy nieco danych:')
show_table(connection)