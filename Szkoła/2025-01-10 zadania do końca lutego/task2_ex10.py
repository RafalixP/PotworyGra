# Kalkulator - prosi użytkownika o dwie liczby i wybrany operator matematyczny, a następnie wykonuje obliczenie i zwraca wynik

#funkcja pobierająca liczbę od użytkownika
def get_number(prompt):
    while True:
        try:
            return float(input(prompt)) #zamieniamy input na typ float aby upewnić się, że użytkownik nie podał niepoprawnego typu np stringa - tylko liczbę da się zamienić na typ float
        except ValueError:
            print("Proszę podać poprawną liczbę.")

#funkcja pobierająca operator od użytkownika
def get_operator():
    while True:
        operator = input("Podaj operator (+, -, *, /): ")
        if operator in ['+', '-', '*', '/']: #sprawdzamy czy użytkownik podał jeden z dostępnych operatorów
            return operator
        else:
            print("Proszę podaj POPRAWNY operator:")

print('Cześć, witaj w programie "Kalkulator". Dokonamy wspólnie pięknych obliczeń!')


#zasadnicza część programu - wykonujemy w pętli dopóki użytkownik jej nie przerwie (tj dopóki nie wybierze 'n' na końcu pętli)
while True:


    # Pobieranie danych od użytkownika
    print()
    number1 = get_number("Podaj pierwszą liczbę: ")
    number2 = get_number("Podaj drugą liczbę: ")
    operator = get_operator()

    # Wykonywanie obliczeń w zależności od tego jaki operator został wybrany
    try:
        if operator == '+':
            result = number1 + number2
        elif operator == '-':
            result = number1 - number2
        elif operator == '*':
            result = number1 * number2
        elif operator == '/':
            result = number1 / number2
        print(f"Wynik: {result}")
    except ZeroDivisionError:
        print("Błąd: Dzielenie przez zero jest niedozwolone.")
    except OverflowError: #błąd zwrócony w przypadku przekroczenia zakresu możliwych wartości dla typu float
        print("Błąd: Przepełnienie liczbowe.")
    except Exception as e: #obsługa innych możliwych, a nie zdefiniowanych tu błędów
        print(f"Błąd: {e}")

    # pytanie do użytkownika, czy chce kontynuować i dokonać kolejne obliczenie
    continue_choice = input("Czy chcesz wykonać kolejne obliczenie? (t/n): ")
    if continue_choice.lower() != 't':
        print("Dziękuję za skorzystanie z kalkulatora!")
        break