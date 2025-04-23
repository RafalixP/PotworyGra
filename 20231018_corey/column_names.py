print('Wprowadź nazwy kolumn oddzielone przecinkiem:')

columns = input()

print(columns.split(', '))

'''import csv
with open('columns_short.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for item in csv_reader:
        print(item)'''
