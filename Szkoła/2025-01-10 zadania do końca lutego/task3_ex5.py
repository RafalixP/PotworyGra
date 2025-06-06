# Funkcja konwertująca liczby arabskie na liczby rzymskie
def int_to_roman(num):
    """
    Przypadki testowe:
    >>> int_to_roman(1)
    'I'
    >>> int_to_roman(4)
    'IV'
    >>> int_to_roman(9)
    'IX'
    >>> int_to_roman(58)
    'LVIII'
    >>> int_to_roman(95)
    'XCV'
    >>> int_to_roman(3999)
    'MMMCMXCIX'
    """
    # Lista wartości cyfr/liczb arabskich
    values = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    # Lista odpowiadających im liczb rzymskich
    symbols = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_number = ''   # Zmienna przechowująca wynikową liczbę rzymską
    i = 0   # Zmienna do iteracji po listach values i symbols
    while num > 0:
        # Dodajemy odpowiednią liczbę symboli rzymskich do wyniku
        for _ in range(num // values[i]):
            roman_number += symbols[i]   # Dopisujemy kolejne cyfry rzymskie
            num -= values[i]  # Zmniejszamy wartość num o wartość z listy values
        i += 1  # Przechodzimy do następnej wartości w listach
    return roman_number


if __name__ == "__main__":
    import doctest
    doctest.testmod()  # Uruchamiamy testy wbudowane w docstring

    print("Witaj w programie konwertującym liczby arabskie na liczby rzymskie!")
    print()
    while True:
        number_input = input("Podaj liczbę lub wpisz 'end', aby zakończyć: ")
        if number_input.lower() == 'end':
            break  # Kończymy pętlę, jeśli użytkownik wpisze 'end'
        try:
            number = int(number_input)  # Konwertujemy input na liczbę całkowitą
            if number < 0 or number == 0:
                print("Zapomniałem powiedzieć, ale program przyjmuje wyłącznie dodatnie liczby.")
            else:
                print(f"Liczba rzymska dla {number} to {int_to_roman(number)}")
        except ValueError:
            print("Proszę podać poprawną liczbę.")  # Obsługa błędu w przypadku niepoprawnego inputu
        
    print("Dziękuję za skorzystanie z programu!")