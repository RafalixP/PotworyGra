import random

print('Zagrajmy w zgadywanie liczb')
print()
print('Dolna granica przedziału to 1')
print('Podaj liczbę która ma być górną granicą przedziału: ')
top_limit = int(input())
print('OK, wylosujemy teraz liczbę z zakresu od 1 do', top_limit,". Twoim zadaniem jest ogdadnięcie jaka liczba została wylosowana.")

losowa_liczba = random.randint(1, top_limit)
print()
#print("Podpowiedź: ", losowa_liczba)   #tego nie pokazywać userowi
print()

print('Zatem, spróbuj odgadnąć jaka liczba została wylosowana przez komputer')
user_guess = int(input('Tu podaj Twój typ: '))

licznik_prob = 0

if user_guess == losowa_liczba:
    print('Gratulacje! Jesteś szybkim strzelcem')
    #print('Wylosowana liczba to: ', losowa_liczba)
    licznik_prob += 1
else:
    while user_guess != losowa_liczba:
        licznik_prob += 1
        print("Pudło!")
        print("To była próba numer: ", licznik_prob)
        if user_guess > losowa_liczba:
            print('Strzelasz zbyt wysoko. Podaj mniejszą wartość')
        else:
            print('Strzelasz zbyt nisko. Podaj większą wartość')
        print()
        user_guess = int(input("Spróbuj jeszcze raz, uwzględniając powyższą wskazówkę: "))
        continue

if licznik_prob == 1:
    print('Wylosowana liczba to: ', losowa_liczba)
    print("Byłeś naprawdę bardzo szybki, to była tylko ", licznik_prob, " próba")
else:
    print('Wylosowana liczba to: ', losowa_liczba, "no w końcu udało Ci się zgadnąć")
    print("Ale zajeło Ci to tyle prób: ", licznik_prob)