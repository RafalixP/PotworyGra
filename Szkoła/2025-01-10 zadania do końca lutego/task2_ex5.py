import random

# witamy użytkownika, prosimy o podanie liczby rund które chciałby zagrać

def greet_user(): 
    print("Cześć! Witaj w grze 'Kamień, Papier, Nożyce' ")
    while True:
        try:
            rounds = int(input("Ile rund chciałbyś zagrać? "))
            if rounds <= 0:
                print("To nie ma sensu, podaj dodatnią wartość.")
            else:
                return rounds
        except ValueError:
            print("Błąd: Podaj proszę liczbę całkowitą.")

#pozyskujemy od użytkownika jego wybór w formie pierwszej litery: k/p/n
def get_user_choice():
    choice_map = {
        "k": "kamień",
        "p": "papier",
        "n": "nożyce"
    }
    while True:
        user_input = input("Wybierz kamień (k), papier (p) lub nożyce (n): ").lower()
        if user_input in choice_map:
            return choice_map[user_input] #zwracamy wybór na podstawie litery podanej przez użytkownika używając słownika choice_map
        else:
            print("Błędny wybór. Wybierz 'k' dla kamień, 'p' dla papier, lub 'n' dla nożyce.")

#komputer "wybiera"
def get_computer_choice():
    choices = ["kamień", "papier", "nożyce"]
    return random.choice(choices)

#porównujemy wybór użytkownika i komputera
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "remis"
    elif (user_choice == "kamień" and computer_choice == "nożyce") or \
         (user_choice == "nożyce" and computer_choice == "papier") or \
         (user_choice == "papier" and computer_choice == "kamień"):
        return "użytkownik"
    else:
        return "komputer"

#funkcja sładająca wszystkie poprzednie w logiczną całość
def play_game():
    rounds = greet_user()  #ilość rund podana przez użytkownika
    user_score = 0
    computer_score = 0
    history = [] #tu będziemy zapisywać wyniki z kolejnych rund

    for round in range(1, rounds + 1):  #pętla iterująca przez kolejne rundy
        print(f"\nRunda {round}")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice) #tu ustalamy kto wygrał daną rundę
        history.append((user_choice, computer_choice, winner)) #tu zapisujemy wyniki z danej rundy
        if winner == "użytkownik":
            user_score += 1  #dodajemy punkt użytkownikowi
            print(f"Wybrałeś {user_choice}, a komputer wybrał {computer_choice}. Wygrywasz!")
        elif winner == "komputer":
            computer_score += 1  #dodajemy punkt komputerowi
            print(f"Wybrałeś {user_choice}, a komputer wybrał {computer_choice}. Przegrywasz!")
        else:
            print(f"Wybrałeś {user_choice}, a komputer wybrał {computer_choice}. Remis!")

    #zestawienie wszystkich rund
    print("\nPodsumowanie gry:")
    for round, (user_choice, computer_choice, winner) in enumerate(history, start=1):
        if winner == "remis":
            print(f"Runda {round}: Wybrałeś {user_choice}, komputer wybrał {computer_choice} - Remis!")
        else:
            print(f"Runda {round}: Wybrałeś {user_choice}, komputer wybrał {computer_choice} - {winner.capitalize()} wygrał")

    #podsumowanie
    print(f"\nWynik końcowy:")
    print(f"Użytkownik: {user_score} punktów")
    print(f"Komputer: {computer_score} punktów")
    if user_score > computer_score:
        print("Gratulacje! Wygrałeś grę!")
    elif user_score < computer_score:
        print("Niestety, przegrałeś grę. Spróbuj ponownie!")
    else:
        print("Remis!")

#pętla while umożliwia użytkownikowi powtórną grę bez konieczności ponownego włączania aplikacji
def main():
    while True:
        play_game()
        again = input("\nCzy chcesz zagrać jeszcze raz? (t/n): ").lower()
        if again != 't':
            print("Dzięki za grę! Do zobaczenia!")
            break

if __name__ == "__main__":
    main()