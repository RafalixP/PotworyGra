# Funkcja obliczająca średnią arytmetyczną
def calculate_mean(numbers):
    return sum(numbers) / len(numbers) if numbers else 0 #dzielimy sumę elemtentów listy przez ilość tychże elementów, o ile lista nie jest pusta

# Powitanie użytkownika
print("Cześć! Ten program obliczy dla Ciebie średnią arytmetyczną podanych liczb")


while True:
    numbers = []

    while True:
        # Pobranie liczby od użytkownika
        user_input = input("Podaj liczbę (jedną na raz) lub wpisz 'dość', aby zakończyć: ") #pobieramy liczby do kalkulacji
        
        if user_input.lower() == 'dość': # jeśli użytownik wpisał 'dość' to kończymy tą pętlę i przechodzimy do kalkulacji
            break
        
        try:
            number = float(user_input) #tu upewniamy się, że user wpisał faktycznie liczbę, a nie np stringa
            numbers.append(number) #i jeśli jest to liczba, to dołączamy ją do listy
        except ValueError: #błąd wyskoczy jeśli użyszkodnik poda coś innego niż liczba
            print("Proszę podać poprawną liczbę.")

    # Obliczenie średniej arytmetycznej
    mean = calculate_mean(numbers) #zmienna 'mean' przyjmuje wartość wyniku działania funkcji 

    # Wyświetlenie wyniku
    print(f"Średnia arytmetyczna podanych liczb to: {mean}")

    # Zapytanie użytkownika, czy chce uruchomić program ponownie
    continue_program = input("Czy chcesz obliczyć średnią dla kolejnych liczb? (t/n): ")
    if continue_program.lower() != 't':
        print("Dziękuję za skorzystanie z programu! Do zobaczenia!")
        break