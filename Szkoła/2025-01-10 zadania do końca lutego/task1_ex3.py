def weight_calculation():
    '''Funcja przeliczająca wagę w zależności od wybranej przez użytkownika planety docelowej'''
    
    # Pytamy użytkownika o jego wagę na Ziemi
    earth_weight = float(input("Podaj swoją wagę na Ziemii (kg): "))
    
    while True:
        # Wyświetlamy menu wyboru planet
        print("\nWybierz planetę, aby obliczyć swoją wagę na tej planecie:")
        print("1. Merkury")
        print("2. Wenus")
        print("3. Ziemia")
        print("4. Mars")
        print("5. Jowisz")
        print("6. Saturn")
        print("7. Uran")
        print("8. Neptun")
        
        # Zapytaj użytkownika o wybór planety
        choice = int(input("\nWpisz numer odpowiadający wybranej planecie i wciśnij ENTER: "))
        
        # Struktura warunkowa obsługująca wybór użytkownika
        if choice == 1:
            planet_name = "Merkury"
            gravity = 0.38
        elif choice == 2:
            planet_name = "Wenus"
            gravity = 0.91
        elif choice == 3:
            planet_name = "Ziemia"
            gravity = 1.00
        elif choice == 4:
            planet_name = "Mars"
            gravity = 0.38
        elif choice == 5:
            planet_name = "Jowisz"
            gravity = 2.34
        elif choice == 6:
            planet_name = "Saturn"
            gravity = 1.06
        elif choice == 7:
            planet_name = "Uran"
            gravity = 0.92
        elif choice == 8:
            planet_name = "Neptun"
            gravity = 1.19
        else:
            print("\nNieprawidłowy wybór. Spróbuj ponownie.")
            continue
        
        weight_on_planet = earth_weight * gravity
        print(f"\nTwoja waga na planecie {planet_name} wynosi: {weight_on_planet:.2f} kg")
        
        # Pytamy użytkownika, czy chce przeliczyć wagę ponownie
        repeat = input("\nCzy chcesz przeliczyć wagę ponownie? (t/n): ").strip().lower()
        if repeat != 't':
            print("\nDziękuję za skorzystanie z programu")
            break

print()
print('Program pozwalający przeliczyć podaną wagę na Ziemii na odpowiadającą wagę na jednej z pozostałych planet naszego Układu Słonecznego')
print('-----------------------------------------')

weight_calculation()