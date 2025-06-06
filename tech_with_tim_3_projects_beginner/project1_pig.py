import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players")
    else:
        print("Invalid, try again, enter the number, not a string")

max_score = 50
player_scores = [0 for _ in range(players)]

#print(player_scores)

while max(player_scores) < max_score:
    for players_index in range(players):
        print("\nPlayer", players_index + 1, "turn has just started!\n")
        current_score = 0
        print('\nYour current score is: ', player_scores[players_index], '\n')

        while True:
            
            should_roll = input('Would you like to roll (y)? ')
            if should_roll.lower() != "y":
                break

            value = roll()    
            if value == 1:
                print('You rolled a 1! Turn done!')
                current_score = 0
                break
            else:
                current_score += value
                print('You rolled a: ', value)

            print("your score is: ", current_score)

        player_scores[players_index] += current_score
        print('Your total is: ', player_scores[players_index])

max_score = max(player_scores)
winning_index = player_scores.index(max_score) + 1
print('Player number', winning_index, 'is the winner with the score ', max_score)




















'''print('Zagrajmy.')
total_score = 0
print("Twój bieżący wynik to: ", + total_score)


losowa_liczba = random.randint(1, 6)
while losowa_liczba >1:
    
    total_score = total_score + losowa_liczba
    print("Twój bieżący wynik to: ", + total_score)
    print("Wyrzuciłeś następującą liczbę: ", losowa_liczba)
    decision = input("Would you like to try another roll? Y/N: ")
    continue

    if losowa_liczba == 1:
        print("Przegrałeś wszystko, Twój wynik to zero")
    break'''