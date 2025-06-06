def C_F_conversion():
    '''Funcja przeliczająca wartość podaną w stopniach Celsiusza na Fahrenheity'''
    

    print('Wpisz wartość temperatury wyrażoną w stopniach Celsiusza i wciśniej ENTER aby przeliczyć ją na Fahrenheity: ')
    celsius_temp = float(input())       #zamieniamy podaną przez użytkownika wartosć na typ float
    fahrenheit_temp = (celsius_temp * 9/5) + 32     #wzór służący do konwersji C -> F i przypisanie wyniku konwersji do zmiennej 'fahrenheit_temp'
    print(f'Temperatura {celsius_temp} st C w przeliczeniu na Fahrenheity to: {fahrenheit_temp} F')


print('Konwerter temperatury Celsiusz -> Fahrenheit')
print('-----------------------------------------')

C_F_conversion()
