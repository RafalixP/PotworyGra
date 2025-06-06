'''
2023-12-28
1. Dodać sprawdzanie poprawności kodu, czyli jak user wpiszę głupotę, to będzie info żeby wpisał poprawny kod
2. Po dokonaniu poprawnej konwersji program nie powinien się kończyć, powinien pytać usera czy chce dokonać kolejnej konwersji'''

import requests

BASE_URL = "http://api.nbp.pl/api"
RATE_TABLE = "/exchangerates/tables/a/"

currencies = requests.get(BASE_URL + RATE_TABLE).json()

wybranaWalutaKod = input('Podaj walutę jakiej kurs chcesz poznać. Podaj trzyliterowy kod: ')

for currency in currencies[0]['rates']:   #dlaczego to działa nawet wtedy kiedy podam prawdziwą walutę
    if wybranaWalutaKod != currency['code']:
        print("Niestety, nie ma waluty o takim kodzie")
        break

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
