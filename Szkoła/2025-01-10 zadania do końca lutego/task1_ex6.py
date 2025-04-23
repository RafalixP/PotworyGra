# Powitanie
print("Cześć! Jestem programem do analizy numeru PESEL.")

while True:
    name = input("Jak masz na imię? ")
    pesel = input("Podaj swój numer PESEL: ")

    # Walidacja długości i typu znaków
    if len(pesel) != 11 or not pesel.isdigit():
        print("Numer PESEL musi mieć 11 cyfr i nie może zawierać liter.")
        continue

    # Wyciągamy datę urodzenia
    year = int(pesel[0:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])

    # Korekta roku i miesiąca w zależności od stulecia
    if month > 80:
        year += 1800
        month -= 80
    elif month > 60:
        year += 2200
        month -= 60
    elif month > 40:
        year += 2100
        month -= 40
    elif month > 20:
        year += 2000
        month -= 20
    else:
        year += 1900

    # Wyodrębnienie liczby porządkowej, płci i cyfry kontrolnej
    ordinal_number = pesel[6:10]
    
    # Określanie płci
    if int(pesel[9]) % 2 == 0:
        sex = "kobieta"
    else:
        sex = "mężczyzna"
    
    #Cyfra kontrolna
    check_digit = pesel[10]

    # Wyświetlenie informacji
    print(f"Imię: {name}\nData urodzenia: {day:02d}/{month:02d}/{year}\nLiczba porządkowa: {ordinal_number}\nPłeć: {sex}\nCyfra kontrolna: {check_digit}")

    # Pytanie o kolejną osobę
    another = input("Czy chcesz przetłumaczyć PESEL dla innej osoby? (t/n): ")
    if another.lower() != 't':
        print("Do widzenia!")
        break