import random

print("Witaj w grze")
user_wins = 0
computer_wins = 0
no_of_attempts = 0

options = ["rock", "paper", "scissors"]
# 0:"rock", 1:"paper", 2:"scissors"

user_plays = input('Do you want to play? Y/N ').lower()

while user_plays == "n":
    print('No to wychodzimy z gry')
    break
else:
    print('Ile rund chcesz zagrać?')
    max_no_of_attempts = int(input())


    while no_of_attempts < max_no_of_attempts:
        computer_pick = options[random.randint(0, 2)]
        user_pick = input("Please choose rock/paper/scissors: ").lower()
        if user_pick not in options:
            print('It\'s not an option. I quit!')
            break

        if user_pick == "rock" and computer_pick == "scissors":
            print('Komputer wybral: ', computer_pick)
            print('User wybral: ', user_pick)
            print('Congrats! You have won')
            user_wins += 1
            no_of_attempts += 1
            print('To była runda: ', no_of_attempts)
            continue
        elif user_pick == "paper" and computer_pick == "rock":
            print('Komputer wybral: ', computer_pick)
            print('User wybral: ', user_pick)
            print('Congrats! You have won')
            user_wins += 1
            no_of_attempts += 1
            print('To była runda: ', no_of_attempts)
        elif user_pick == "scissors" and computer_pick == "paper":
            print('Komputer wybral: ', computer_pick)
            print('User wybral: ', user_pick)
            print('Congrats! You have won')
            user_wins += 1
            no_of_attempts += 1
            print('To była runda: ', no_of_attempts)
        else:
            print('Komputer wybral: ', computer_pick)
            print('User wybral: ', user_pick)
            print('Przykro mi, punkt dla komputera')
            computer_wins += 1
            no_of_attempts += 1
            print('To była runda: ', no_of_attempts)
print('To koniec. Nieco statystki:')
print('Punkty usera: ', user_wins)
print('Punkty komputera: ', computer_wins)
