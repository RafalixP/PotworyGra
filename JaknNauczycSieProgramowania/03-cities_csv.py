import csv

with open('cities.csv') as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        print(row['City'])