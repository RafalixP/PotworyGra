print("Witaj szanowny userze")
print("Czy chcesz zagrać?")
czyChce = input('T/N? ')

if czyChce == "T":
    wynik = 0
    licznik_pytan = 0
    print("Twój bieżący wynik to:", wynik)
    print("Do tej pory odpowiedziałeś na następującą liczbę pytań: ", licznik_pytan)
    print("Pytanie 1: Jaka jest odpowiedź")

    odp1 = input("Tu podaj opdowiedź na pytanie 1: ")
    #print(odp1)
    licznik_pytan += 1
    if odp1 == "popr_odp1":
        print("Brawo! To jest poprawna odpowiedź")
        wynik += 1
    else:
        print("Przykra sprawa, ale nie zgadłeś")
        print()
        print("Twój bieżący wynik w tej rundzie to: ", wynik)
    print()
    print("Do tej pory odpowiedziałeś na następującą liczbę pytań: ", licznik_pytan)

    odp2 = input("Tu podaj opdowiedź na pytanie 2: ")
    #print(odp2)
    licznik_pytan += 1
    
    if odp2 == "popr_odp2":
        print("Brawo! To jest poprawna odpowiedź na drugie pytanie")
        wynik += 1
    else:
        print("Przykra sprawa, ale nie zgadłeś")
        print()
        print("Twój bieżący wynik w tej rundzie to: ", wynik)
    print()
    print("Do tej pory odpowiedziałeś na następującą liczbę pytań: ", licznik_pytan)
    print("To było ostatnie pytanie")

    if wynik >= 1:
        print("Zdobyte punkty:", wynik)
        print("To znaczy że nie jesteś najgorszy")
    else:
        print("Zdobyte punkty:", wynik)
        print("To jest totalne dno")
    print()
    print("Zdobyłeś ", (wynik/licznik_pytan*100), "% punktów")
else:
    print("Nie ma sprawy, może innym razem")
    quit()

