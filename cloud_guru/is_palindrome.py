# 3) Write function to check if a string is a palindrome

def is_palindrome():
    a_word = str(input('Podaj proszę Twoje słowo do sprawdzenia: '))
    reverse_word = ''.join(reversed(a_word))
    print('Twoje słowo napisane od tyłu to: ',reverse_word)
    if a_word == reverse_word:
        print('To słowo JEST palindromem')
    elif a_word != reverse_word:
        print('To słowo nie jest palindromem')
    else:
        print('Wprowadź poprawnie słowo')
    
while True:    
    is_palindrome()
    