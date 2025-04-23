def main(input_func=input):
    while True:
        print("Cześć! Wprowadź proszę czas lub wpisz 'koniec', aby zakończyć.")
        print()

        # pobieramy czas od użytkownika
        time_input = input_func("Wprowadź czas (HH:MM): ")

        if time_input.lower() == 'koniec':
            print("Do widzenia!")
            break

        try:
            # zamieniamy czas na liczbę godzin i liczbę minut
            hours, minutes = map(int, time_input.split(":"))

            # liczymy ilość kwadransów
            total_minutes = hours * 60 + minutes
            quarters = total_minutes // 15

            # wyświetlamy wynik
            print(f"Liczba kwadransów zawierająca się w podanym czasie: {quarters}")

        except ValueError:
            print("Błąd: Upewnij się, że czas jest poprawnie podany w formacie HH:MM.")

if __name__ == "__main__":
    main()