print("Cześć! Sprawdźmy, czy słowo o którym myślisz jest palindromem.")

while True: #wykonujemy tą pętlę dopóki użytkownik nie powie 'n' na jej końcu

    word = input("Podaj słowo: ")

     # Sprawdzenie, czy wpisane znaki to cyfry
    if any(char.isdigit() for char in word):
        print("Słowo nie może zawierać cyfr. Spróbuj ponownie.")
        continue

    if word == word[::-1]:  # Sprawdzenie, czy słowo jest palindromem tj czy przeliterowane wspak jest takim samym stringiem jak słowo wejściowe
        print(f"Tak, słowo '{word}' jest palindromem.")
    else:
        print(f"Nie, słowo '{word}' nie jest palindromem.")

    # Pytanie o kolejne słowo
    another = input("Czy chcesz sprawdzić inne słowo? (t/n): ")
    if another.lower() != 't':
        print("Do widzenia!")
        break