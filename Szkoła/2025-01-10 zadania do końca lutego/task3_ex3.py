# Program do zarządzania zapasami w sklepie

# Słownik zawierający kody produktów i ich wartości
inventory = {
    "P001": "Produkt 1 - $10",
    "P002": "Produkt 2 - $15",
    "P003": "Produkt 3 - $20",
    "P004": "Produkt 4 - $25",
    "P005": "Produkt 5 - $30"
}

# Funkcja do wyświetlania wartości produktu na podstawie kodu
def get_product_value(code):
    """
    Zwraca wartość produktu na podstawie kodu.
    Przykładowe wartości testowe i oczekiwane rezultaty:
    >>> get_product_value("P001")
    'Produkt 1 - $10'
    >>> get_product_value("p002")
    'Produkt 2 - $15'
    >>> get_product_value("P006")
    'Nieprawidłowy kod produktu'
    >>> get_product_value("p007")
    'Nieprawidłowy kod produktu'
    """
    return inventory.get(code.upper(), "Nieprawidłowy kod produktu")

if __name__ == "__main__":
    import doctest
    doctest.testmod() #funkcja która uruchamia testy zapisane w docstringach 

    print('Cześć, witaj w naszym sklepie, mamy tutaj strasznie dużo produktów!')
    print()

    # Główna pętla programu
    while True:
        # Pobieranie kodu produktu od użytkownika
        code = input("Podaj kod produktu (P00x) aby poznać jego cenę lub wpisz 'end', aby zakończyć: ")
        
        # Sprawdzenie, czy użytkownik chce zakończyć program
        if code.lower() == "end":
            print("Do widzenia, zapraszamy ponownie.")
            break
        
        # Wyświetlanie wartości produktu
        print(get_product_value(code))