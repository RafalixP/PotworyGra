name = input('Type your name: ')
print('Welcome', name, 'to this adventure')

answer = input("Do you want to go left or right? ").lower()

if answer == "left":
    answer = input('You come to a river, you can walk around it or swim across. Walk/swim ? ').lower()

    if answer == "swim":
        print('You swam across and were eaten by alligator.')
    elif answer == "walk":
        print('You\'ve walked for many miles and ran out of the water')
    else:
        print('Not a valid option, you lose')
    
elif answer == "right":
    answer = input('You come to a bridge. It looks wobbly, do you want to cross it or head back (cross/back)').lower()
    if answer == "back":
        print('You go back and lose')
    elif answer == "cross":
        answer = input('you crossed the bridge and met a stranger. Do you talk with him? (Yes/No) ').lower()
        if answer == "yes":
            print('You talkked to the stranger and he gave you gold. You win.')
        elif answer == "no":
            print('You ignore a stranger, he is offended and you lose')
        else:
            print('Not a valid option, you lose')
    else:
        print('Not a valid option, you lose')
else:
    print('Not a valid option, you lose')

print('Thank you', name, 'for tryin\' ')