import requests

BASE_URL = "http://api.nbp.pl/api"
RATE_TABLE = "/exchangerates/tables/a/"

currencies = requests.get(BASE_URL + RATE_TABLE).json()

tabela = currencies[0]
obiekt = tabela.get(table)
print(obiekt)

        