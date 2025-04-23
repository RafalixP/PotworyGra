def VAT_calculation():
    '''Funcja obliczająca wartość podatku VAT oraz cenę brutto na podstawie ceny netto podanej przez użytkownika'''
    netto_price = 211    #cena netto jest stała w tym przypadku

    print(f'Cena netto butów to {netto_price:.2f} PLN')

    VAT_value = 0.23*netto_price
    brutto_price = netto_price+VAT_value

    print(f'Wartość podatku VAT to {VAT_value} PLN')
    print(f'Całkowita cena butów po uwzględnieniu podatku VAT to {brutto_price} PLN')


print()
print('Program liczący wartość podatku VAT oraz cenę brutto ')
print('-----------------------------------------')

VAT_calculation()
