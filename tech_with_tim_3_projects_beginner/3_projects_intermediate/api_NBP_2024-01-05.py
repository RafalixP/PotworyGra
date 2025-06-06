'''
1. Funkcja wyświetlająca tabelę wszystkich walut symbol - kurs
2. Funkcja przeliczenia wybranej waluty na PLN'''

import requests

BASE_URL = "http://api.nbp.pl/api"
RATE_TABLE = "/exchangerates/tables/a/"

currencies = requests.get(BASE_URL + RATE_TABLE).json()


def tabelaWalut(currencies):
    for currency in currencies[0]['rates']:
        print(currency['code'])
        #print(currency['currency'])
        print(currency['mid'])
        print('-' * 10)

def kalkulatorWalut():
    pass

print('Witaj userze. Co chcesz zrobić?')
print('Wpisz słowo \'tabela\' aby wyświetlić tabelę walut wraz z kursami')
print('Wpisz słowo \'kalkulator\' aby użyć kalkulatora walut')
print('Wpisz \'q\' aby zakończyć działanie programu')
print()

while True:
    zadanie = input('Jakiej funkcji chciałbyś użyć? ').lower()

    if zadanie == 'q':
        print("Do widzenia")
        break
    elif zadanie == "tabela":
        tabelaWalut(currencies)
    elif zadanie == "kalkulator":
        print("Wybrałeś kalkulator walut")

        wybranaWalutaKod = input('Podaj walutę jakiej kurs chcesz poznać. Podaj trzyliterowy kod: ')

        for currency in currencies[0]['rates']:   #dlaczego to działa nawet wtedy kiedy podam prawdziwą walutę
            if wybranaWalutaKod != currency['code']:
                print("Niestety, nie ma waluty o takim kodzie")
                break
            else:
                quantity = int(input('Ile waluty chcesz wymienić? '))

                print(" ")
                print('Wybrana waluta to: ', wybranaWalutaKod)

                print('Ilość do wymiany: ', quantity)

                for currency in currencies[0]['rates']:
                    if wybranaWalutaKod == currency['code']:
                        print("Kurs wymiany to: ", float(currency['mid']))
                        result = quantity * float(currency['mid'])
                        print(f'W rezultacie otrzymasz {result}.')
                        break
    else:
        print('Wpisałeś niepoprawną wartość. Popraw się lub wpisz \'q\' aby zakończyć program.')
        #break            

