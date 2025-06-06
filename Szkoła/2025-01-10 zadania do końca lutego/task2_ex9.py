import random
import string

#powitanie
def greet_user():
    print("Witaj w grze w wisielca!")

#słownik z którego losujemy słowa do gry
def choose_word():
    words = ["python", "programowanie", "komputer", "algorytm", "kodowanie"]
    return random.choice(words)

#funkcja wyświetlająca podkreślenia oraz litery które zostały już odgadnięte przez użytkownika
def display_game_state(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

#walidacja inputu: odrzucamy inputy dłuższe niż jedna litera
def validate_input(guess):
    if len(guess) != 1 or guess not in string.ascii_lowercase:
        return False
    return True

#gra zasadnicza
def hangman_game(score):
    word = choose_word() #to jest nasze wylosowane słowo
    guessed_letters = [] #na początku nie ma żadnych literek odgadniętych przez użytkownika
    attempts = 7

    #pętla przez którą przechodzimy dopóki użytkownikowi nie skończą się wolne próby
    while attempts > 0:
        print("\nSłowo: ", display_game_state(word, guessed_letters)) #wyświetlamy podkreślenia oraz odgadnięte litery, jeśli jakieś są
        guess = input("Zgadnij literę: ").lower() #bierzemy input od użytkownika

        #walidacja inputu
        if not validate_input(guess):
            print("Nieprawidłowe dane. Wprowadź jedną literę (bez cyfr i znaków specjalnych).")
            continue

        if guess in guessed_letters:
            print("Już zgadłeś tę literę. Spróbuj ponownie.") #nie obieramy prób jeśli użytkownik ponownie wprowadzi już odgadniętą literę
        elif guess in word:
            guessed_letters.append(guess) #jeśli użytkownik zgadł literę, to dołączamy ją żeby wyświetlić zamiast podkreślenia
            print("Dobrze! Litera", guess, "jest w słowie.")
        else:
            attempts -= 1 #pudło, odejmujemy próbę
            print("Źle! Litera", guess, "nie jest w słowie. Pozostało prób: ", attempts)

        if all(letter in guessed_letters for letter in word): #przypadek kiedy użytkownik zdąrzył odgadnąć wszystkie litery
            print("\nGratulacje! Zgadłeś słowo:", word)
            score += 1 #dodajemy punkt
            break
    else:
        print("\nPrzegrałeś! Słowo to było:", word)

    return score

#główna funkcja
def main():
    greet_user()
    score = 0
    #pętla którą powtarzamy dopóki użytkownik sie nie rozmyśli (i wybierze 'n')
    while True:
        score = hangman_game(score)
        print("Twój aktualny wynik: ", score)
        choice = input("Czy chcesz zagrać ponownie? (t/n): ").lower()
        if choice == 'n':
            print("Dziękujemy za grę! Twój końcowy wynik to:", score)
            break

if __name__ == "__main__":
    main()