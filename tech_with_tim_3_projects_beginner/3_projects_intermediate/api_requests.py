from requests import get
from pprint import PrettyPrinter

BASE_URL = "http://free.currconv.com/"
#GOLD_PRICE = "/cenyzlota"
RATE_TABLE = "/exchangerates/tables/a/"

printer = PrettyPrinter()

#data_gold = get(BASE_URL + GOLD_PRICE).json()
data_rates = get(BASE_URL + RATE_TABLE).json()

def print_currencies(currencies):
    for currency in currencies:
        tableDate = currency['effectiveDate']
        tableNumber = currency['no']
        curRates = currency['rates']
        print(f"{curRates}")

#print(data)
#printer.pprint(data_gold) #cena złota
#printer.pprint(data_rates[0]['rates']) #tabela kursów walut
        
print_currencies(data_rates)

