def calculate_birth_number(birth_date):
    '''Liczy numer urodzenia z podanej daty urodzenia w formacie DD-MM-YYYY'''
    
    # Usuwamy wszystkie znaki niebędące cyframi z daty urodzenia
    digits = [int(char) for char in birth_date if char.isdigit()]
    
    # Sumujemy cyfry aż do uzyskania pojedynczej cyfry
    while len(digits) > 1:
        digits = [int(char) for char in str(sum(digits))]
    
    return digits[0]

def main():
    '''Główna funkcja uruchamiająca program do obliczania numeru urodzenia'''
    
    print("Witaj! Jestem programem do obliczania Twojego numeru urodzenia.")
    
    while True:
        # Zapytaj o imię użytkownika
        name = input("Jak masz na imię? ")
        
        # Zapytaj o rok, miesiąc i dzień urodzenia
        year = input("Podaj rok urodzenia (YYYY): ")
        month = input("Podaj miesiąc urodzenia (MM): ")
        day = input("Podaj dzień urodzenia (DD): ")
        
        # Składanie daty urodzenia w formacie DD-MM-YYYY
        date_of_birth = f"{day}-{month}-{year}"
        
        # Obliczanie numeru urodzenia
        birth_number = calculate_birth_number(date_of_birth)
        
        # Wyświetlanie wyników
        print(f"\nCześć {name}, oto kilka liczb, które mogą Cię zainteresować.")
        print(f"Twoja data urodzenia to: {date_of_birth}")
        print(f"Twój numer urodzenia to: {birth_number}")
        print("Miłego dnia!")
        
        # Zapytaj, czy użytkownik chce obliczyć numer urodzenia dla innej osoby
        repeat = input("\nCzy chcesz obliczyć numer urodzenia dla innej osoby? (t/n): ").strip().lower()
        if repeat != 't':
            print("\nDo widzenia!")
            break

# Uruchomienie głównej funkcji
main()