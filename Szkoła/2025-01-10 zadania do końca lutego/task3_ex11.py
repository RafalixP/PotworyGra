import sqlite3

# Połączenie z bazą danych SQLite (lub utworzenie jej, jeśli nie istnieje)
conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()

# Utworzenie tabeli do przechowywania numerów telefonów
cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    phone_number TEXT NOT NULL
)
''')

def format_phone_number(phone_number):
    # Formatowanie numeru telefonu: zamiana "00" na "+"
    if phone_number.startswith("00"):
        return "+" + phone_number[2:]
    return phone_number

def save_phone_number(phone_number):
    # Formatowanie i zapisywanie numeru telefonu w bazie danych
    formatted_number = format_phone_number(phone_number)
    cursor.execute('INSERT INTO contacts (phone_number) VALUES (?)', (formatted_number,))
    conn.commit()
    return formatted_number

def display_saved_numbers():
    # Wyświetlanie wszystkich zapisanych numerów telefonów
    cursor.execute('SELECT * FROM contacts')
    rows = cursor.fetchall()
    print("Zapisane numery telefonów:")
    for row in rows:
        print(f"{row[0]}: {row[1]}")

# używamy pętli while aby móc dodać wiele numerów
while True:
    phone_number = input("Podaj numer telefonu (lub wpisz 'n' aby zakończyć): ")
    
    if phone_number.lower() == 'n':
        break
    
    # Zapisanie i wyświetlenie sformatowanego numeru telefonu
    formatted_number = save_phone_number(phone_number)
    print(f"Sformatowany numer: {formatted_number}")
    display_saved_numbers()

# Zamknięcie połączenia z bazą danych
conn.close()
