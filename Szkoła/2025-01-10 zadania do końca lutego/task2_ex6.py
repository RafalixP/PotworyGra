import string #biblioteka którą wykorzystamy do operacji na stringach

# witamy użytkownika
def greet_user():
    print("Cześć! Witaj w programie szyfrującym tekst za pomocą szyfru Cezara.")
    text = input("Proszę podaj tekst do zaszyfrowania: ")
    shift = int(input("Podaj liczbę przesunięć: "))
    return text, shift

# funkcja do szyfrowania tekstu
def caesar_cipher(text, shift):
    encrypted_text = [] # do tej listy będziemy dorzucać poszczególne znaki (oryginalne jak i zmienione)
    for char in text: #sprawdzamy każdy ze znaków w naszym stringu
        if char.isalpha(): #sytuacja kiedy znak jest literą
            alphabet = string.ascii_lowercase if char.islower() else string.ascii_uppercase #sięgamy do małych lub wielkich liter ASCII w zależności od tego jaką literę rozpatrujemy
            new_char = alphabet[(alphabet.index(char) + shift) % 26] #tu realizujemy przesunięcie o zadaną liczbę w obrębie alfabetu
            encrypted_text.append(new_char) #dołączamy do listy znak już po przesunięciu
        else:  #sytuacja kiedy znak NIE jest literą (jest cyfrą, spacją etc)
            encrypted_text.append(char) #dołączamy do listy oryginalny znak
    return ''.join(encrypted_text) #przekształcamy listę w stringa

def main():
    text, shift = greet_user()
    encrypted_text = caesar_cipher(text, shift)
    print(f"Zaszyfrowany tekst: {encrypted_text}")

if __name__ == "__main__":
    main()