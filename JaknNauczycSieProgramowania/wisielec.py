import sys
no_of_tries = 5
word = 'kamil'
used_letters = []
user_word = []

def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
    return indexes

def show_state_of_game():
    print()
    print("".join(user_word))
    print('Pozostało prób: ', no_of_tries)
    print('Użyte litery: ',  used_letters)
    print()

for _ in word:
    user_word.append('_')
while True:
    letter = input('Podaj literę: ')
    used_letters.append(letter)

    found_indexes = find_indexes(word, letter)

    if len(found_indexes) == 0:
        print('Nie ma takiej litery')
        no_of_tries -= 1
        #print('Pozostało prób: ', no_of_tries)

        if no_of_tries == 0:
            print('Koniec gry')
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter
        #print(user_word)

        #print("".join(user_word))
        if ''""''.join(user_word) == word:
            print('Brawo, odgadłeś słowo')
            print('Słowo którego szukałeś to: ', word)
            sys.exit(0)

    show_state_of_game()

    #print(word.index(letter))
#    print('Użyte litery: ',  used_letters)