import requests #biblioteka potrzebna do wysyłania requestów do API (w tym przypadku: strony banku)

# Funkcja do pobierania aktualnych kursów walut ze strony NBP
def get_exchange_rate(base_currency, target_currency): #funkcja jako parametry bierze walutę bazową (początkową) oraz walutę docelową (tj ich skróty np USD)
    if base_currency == target_currency:
        return 1  # Kurs wymiany między tą samą walutą to 1
    
    url = f"https://api.nbp.pl/api/exchangerates/rates/a/{base_currency}/?format=json"  #stąd chcemy pozyskać informację o kursie waluty bazowej
    response = requests.get(url)    #wysyłamy request metodą GET i zapisujemy odpowiedź w zmiennej 'response'
    
    try:
        data = response.json()  #konwertujemy odpowiedź z postaci JSONa do słownika Pythonowego
    except requests.exceptions.JSONDecodeError:
        return None
    
    rate = data['rates'][0]['mid']  #wyciągamy wartość kursu ze słownika
    
    if target_currency != 'PLN':
        url_target = f"https://api.nbp.pl/api/exchangerates/rates/a/{target_currency}/?format=json" #stąd chcemy pozyskać informację o kursie waluty docelowej
        response_target = requests.get(url_target)  #wysyłamy request metodą GET i zapisujemy odpowiedź w zmiennej 'response'
        
        try:
            data_target = response_target.json()   #konwertujemy odpowiedź z postaci JSONa do słownika Pythonowego
        except requests.exceptions.JSONDecodeError:
            return None
        
        rate_target = data_target['rates'][0]['mid'] #wyciągamy wartość kursu waluty docelowej ze słownika
        return rate / rate_target #obliczamy ostateczny kurs wymiany
    
    return rate #zwracamy 'rate' w przypadku gdy docelowa waluta to PLN

# Funkcja do przeliczania waluty
def currency_converter(amount, base_currency, target_currency): #funkcja jako parametry bierze walutę bazową, docelową oraz kwotę
    rate = get_exchange_rate(base_currency, target_currency)    #zmienna przyjmuje wartość od funkcji get_exchange_rate
    if rate is None:
        print("Błąd pobierania kursu wymiany. Proszę podać poprawny symbol waluty.") #wyświetla się w sytuacji kiedy np. użytownik podał nieprawidłowy symbol waluty
        return None
    return amount * rate #kalkulacja

# Główna funkcja aplikacji
def main():
    print("Witaj w kalkulatorze walut!")
    print()
    
    while True:
        # Pobranie danych od użytkownika
        while True:
            base_currency = input("Podaj walutę źródłową (np. USD): ").upper()
            target_currency = input("Podaj walutę docelową (np. EUR): ").upper()
            try:
                amount = float(input("Podaj kwotę do przeliczenia: ")) #zmiana na float pozwala upewnić się, że użytownik wprowadził liczbę, a nie np stringa
                if amount < 0: #nie chcę przeliczać kwot mniejszych niż zero 
                    print("Proszę podać kwotę większą od zera.")
                    continue
                break
            except ValueError:
                print("Proszę podać poprawną kwotę.")
        
        
        # Przeliczenie waluty
        converted_amount = currency_converter(amount, base_currency, target_currency)
        if converted_amount is not None:
            # Wyświetlenie wyniku
            print(f"{amount} {base_currency} to {converted_amount:.2f} {target_currency}")
        
        # Zapytanie użytkownika, czy chce wykonać kolejne przeliczenie
        another_calculation = input("Czy chcesz wykonać kolejne przeliczenie? (t/n): ").lower()
        if another_calculation != 't':  #nie chce
            break
    
    print("Dziękujemy za skorzystanie z kalkulatora walut!")

# Uruchomienie aplikacji
if __name__ == "__main__":
    main()