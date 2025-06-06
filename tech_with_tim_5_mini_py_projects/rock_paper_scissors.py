import random

print("Witaj w grze")
max_no_of_attempts = 1 #int(input('Ile rund chcesz zagrać? '))
user_wins = 0
computer_wins = 0
no_of_attempts = 0

options = ["rock", "paper", "scissors"]
# 0:"rock", 1:"paper", 2:"scissors"

computer_pick = options[random.randint(0, 2)]
user_pick = input("Please type: rock/paper/scissors or type Q to quit the game: ").lower()
if user_pick == "q":
    break

while no_of_attempts != max_no_of_attempts:
    if user_pick not in options:
        print('Please provide correct name')
    else:
        if user_pick == "rock" and computer_pick == "scissors":
            print('Komputer wybral: ', computer_pick)
            print('User wybral: ', user_pick)
            print('Congrats! You have won')
            user_wins += 1
            no_of_attempts += 1
        elif user_pick == "paper" and computer_pick == "rock":
            print('Komputer wybral: ', computer_pick)
            print('User wybral: ', user_pick)
            print('Congrats! You have won')
            user_wins += 1
            no_of_attempts += 1
        elif user_pick == "scissors" and computer_pick == "paper":
            print('Komputer wybral: ', computer_pick)
            print('User wybral: ', user_pick)
            print('Congrats! You have won')
            user_wins += 1
            no_of_attempts += 1
        else:
            print('Komputer wybral: ', computer_pick)
            print('IKSUser wybral: ', user_pick)
            print('Przykro mi, punkt dla komputera')
            computer_wins += 1
            no_of_attempts += 1
    
'''if user_pick in options:
    print('Punkty usera: ', user_wins)
    print('Punkty komptera: ', computer_wins)
else:
    print('Koniec gry, spróbuj jeszcze raz')'''