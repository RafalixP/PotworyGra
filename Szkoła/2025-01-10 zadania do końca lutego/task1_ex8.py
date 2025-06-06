print("Cześć! Jestem magicznym pudełkiem. Ile byś rzeczy u mnie nie schował, podwóję ich liczbę (w magiczny sposób! tylko dziś!) każdego nowego dnia")

# Prośba o liczbę przedmiotów
while True:
    items_input = input("Ile przedmiotów chciałbyś schować? Podaj liczbę przedmiotów: ")
    if not items_input.isdigit(): #walidacja
        print("Liczba przedmiotów musi być liczbą całkowitą. Spróbuj ponownie.")
    else:
        items = int(items_input)
        if items < 0:
            print("Masz szczęście, tylko ja ogarniam minusy")
        break

# Prośba o liczbę dni
while True:
    days_input = input("Jak długo chcesz je przechowywać? Podaj liczbę dni: ")
    if not days_input.isdigit(): #walidacja
        print("Liczba dni musi być liczbą całkowitą. Spróbuj ponownie.")
    else:
        days = int(days_input)
        if days < 0:
            print("Masz szczęście, tylko ja ogarniam minusy")
        break

# kalkulacja
for day in range(days):
    items *= 2

# Wyświetlenie końcowej liczby przedmiotów
print(f"Po {days} dniach liczba Twoich przedmiotów to: {items}")