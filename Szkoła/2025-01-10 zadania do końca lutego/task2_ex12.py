# Funkcja konwertująca liczbę na system binarny
def convert_to_binary(number):
    return bin(number)[2:]

print("Cześć! Ten program konwertuje liczby dziesiętne na system binarny.")

while True:
    # Pobranie liczby od użytkownika
    number = int(input("Podaj liczbę, którą chcesz przekonwertować na system binarny: "))

    # Konwersja liczby na system binarny
    result = convert_to_binary(number)

    # Wyświetlenie wyniku
    print(f"Liczba {number} w systemie binarnym to: {result}")

    # Zapytanie użytkownika, czy chce kontynuować
    continue_conversion = input("Czy chcesz przekonwertować kolejną liczbę? (t/n): ")
    if continue_conversion.lower() != 't':
        print("Dziękuję za skorzystanie z programu! Do zobaczenia!")
        break