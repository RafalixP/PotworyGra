from requests import get

BASE_URL = "http://api.nbp.pl/api"
RATE_TABLE = "/exchangerates/tables/a/"

data_rates = get(BASE_URL + RATE_TABLE)
currencies = data_rates.json()

def waluty(currencies):
    for currency in currencies[0]['rates']:
        print(currency['code'])
        print(currency['currency'])
        print(currency['mid'])
        print('-' * 10)

waluty(currencies)


'''BASE_URL = "http://api.nbp.pl/api"
RATE_TABLE = "/exchangerates/tables/a/"

data_rates = get(BASE_URL + RATE_TABLE).json()

print(data_rates)'''