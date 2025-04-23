import random
import time

#funkcja losująca
def coin_toss():
    return random.choice(['orzełek', 'reszka'])

#funkcja główna
def heads_or_tails_game():
    print("Witaj w grze orzełek czy reszka!")
    
    #początkowa ilość punktów 
    points = 0
    
    #pętlę wykonujemy dopóki user nie przerwie wpisując 'end'
    while True:
        #użytkownik wybiera
        print(f"Twoje punkty: {points}")
        user_choice = input("Wpisz swój wybór (o/r) lub 'end', aby zakończyć: ").lower()
        
        #przypadek kiedy użytkownik chce skończyć grę
        if user_choice == 'end':
            print(f"Dziękujemy za grę! Twoje końcowe punkty: {points}")
            break
        
        if user_choice == 'o':
            full_choice = 'orzełek'
        elif user_choice == 'r':
            full_choice = 'reszka'
        else:
            print("Nieprawidłowy wybór. Proszę wpisać 'o' dla orzełka lub 'r' dla reszki.")
            continue
        
        print(f'Twój wybór to {full_choice}')
        print("Rzucam monetą za")
        print('3...')
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        
        #wykorzystujemy funkcję losującą
        result = coin_toss()
        print(f"Wynik rzutu to {result}")
        
        if (user_choice == 'o' and result == 'orzełek') or (user_choice == 'r' and result == 'reszka'):
            print("Gratulacje! Punkt dla Ciebie.")
            points += 1
        else:
            print("Niestety, nie trafiłeś, może następnym razem będziesz mieć więcej szczęścia.")
        
        print()

# Rozpoczynamy grę
heads_or_tails_game()