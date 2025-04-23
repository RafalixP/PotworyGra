import sys
import random
import string

password = []
characters_left = -1

def update_characters_length(number_of_characters):
    global characters_left

    if number_of_characters <0 or number_of_characters > characters_left:
        print('liczba podanych znaków spoza przedziału 0, ', characters_left)
        sys.exit(0)
    else:
        characters_left -= number_of_characters


password_lenght = int(input('Jak długie ma być hasło? '))

if password_lenght < 5:
    print('Hasło jest za krótkie. Hasło powinno mieć przynajmniej znaków. Spróbuj jeszcze raz')
    sys.exit(0)
else:
    characters_left = password_lenght
    print('Pozostało znaków: ', characters_left)

lowercase_letters = int(input('Ile mały liter ma mieć hasło? '))

update_characters_length(lowercase_letters)

uppercase_letters = int(input('Ile wielkich liter ma mieć hasło? '))

update_characters_length(uppercase_letters)

special_characters = int(input('Ile znaków specjalnych ma zawierać hasło? '))

update_characters_length(special_characters)

digits = int(input('Ile cyfr ma mieć hasło? '))    

update_characters_length(digits)
                        
if characters_left > 0:
    print()
    print('Nie wszystkie znaki zostały wykorzystane. Hasło zostanie uzupełnione małymi literami')
    lowercase_letters += characters_left

print()
print('Długość hasła: ', password_lenght)
print('Małe litery:, ', lowercase_letters)
print('Wielkie litery: ', uppercase_letters)
print('Znaki specjalne: ', special_characters)
print('Cyfry: ', digits)

for _ in range(password_lenght):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1
    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -= 1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1

random.shuffle(password)
print('Twoje tajne hasło to: ', "".join(password))