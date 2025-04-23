# lista dań w formie słownika
dishes = {
    1: ("Kasza gryczana z warzywami", 200),
    2: ("Kasza jaglana z owocami", 250),
    3: ("Ryż brązowy z kurczakiem i brokułami", 350),
    4: ("Makaron pełnoziarnisty z sosem pomidorowym i tofu", 400),
    5: ("Ziemniaki pieczone z fasolą i warzywami", 300),
    6: ("Sałatka z soczewicą i warzywami", 250),
    7: ("Ryba ze słoika z kaszą gryczaną i warzywami", 350)
}

# Funkcja do obliczania BMR - podstawowej przemiany materii - wzór Mifflina-St Jeora
def calculate_bmr(weight, height, age, gender):
    if gender == 'm':
        return 10 * weight + 6.25 * height - 5 * age + 5
    elif gender == 'k':
        return 10 * weight + 6.25 * height - 5 * age - 161
    else:
        return None

# Korekta zapotrzebowania energetycznego w zależności od poziomu aktywności
def calculate_caloric_needs(bmr, activity_level):
    if activity_level == 'niski':
        return bmr * 1.2
    elif activity_level == 'średni':
        return bmr * 1.55
    elif activity_level == 'wysoki':
        return bmr * 1.725
    else:
        return None

# obliczanie różnicy kalorycznej
def calculate_caloric_difference(caloric_needs, caloric_intake):
    return caloric_intake - caloric_needs

# Funkcja do pobierania danych od użytkownika
def get_user_data():
    age = int(input("Podaj swój wiek: "))
    weight = float(input("Podaj swoją wagę (kg): "))
    height = float(input("Podaj swój wzrost (cm): "))
    gender = input("Podaj swoją płeć (m/k): ").lower()
    activity_level = input("Podaj swój poziom aktywności fizycznej (niski/średni/wysoki): ").lower()
    return age, weight, height, gender, activity_level

# Funkcja do pobierania informacji o spożytych daniach od użytkownika
def get_user_dishes():
    caloric_intake = 0
    print("\nLista dostępnych dań:")
    for number, (dish_name, calories) in dishes.items():
        print(f"{number}. {dish_name} - {calories} kcal")

    print("\nPodaj numery spożytych dań (wpisz '0', aby zakończyć):")
    while True:
        dish_number = int(input("Numer dania: "))
        if dish_number == 0:
            break
        if dish_number in dishes:
            caloric_intake += dishes[dish_number][1]
        else:
            print("Nieznany numer dania. Spróbuj ponownie.")
    return caloric_intake

# Główna funkcja aplikacji
def main():
    age, weight, height, gender, activity_level = get_user_data()
    bmr = calculate_bmr(weight, height, age, gender)
    if bmr is None:
        print("Błąd: Nieprawidłowa płeć. Podaj 'm' lub 'k'.")
        return

    caloric_needs = calculate_caloric_needs(bmr, activity_level)
    if caloric_needs is None:
        print("Błąd: Nieprawidłowy poziom aktywności fizycznej. Podaj 'niski', 'średni' lub 'wysoki'.")
        return

    caloric_intake = get_user_dishes()
    caloric_difference = calculate_caloric_difference(caloric_needs, caloric_intake)

    print(f"\nTwoje zapotrzebowanie kaloryczne wynosi: {caloric_needs:.2f} kcal")
    print(f"Twoje spożycie kalorii wynosi: {caloric_intake} kcal")
    if caloric_difference > 0:
        print(f"Masz nadmiar kalorii: {caloric_difference:.2f} kcal")
    elif caloric_difference < 0:
        print(f"Masz niedobór kalorii: {-caloric_difference:.2f} kcal")
    else:
        print("Jesz tyle ile potrzebujesz, tak trzymaj!")

print()
print('Jesz za dużo? Jesz za mało? A może jesz tyle ile trzeba? Sprawdź!')
print()

if __name__ == "__main__":
    main()