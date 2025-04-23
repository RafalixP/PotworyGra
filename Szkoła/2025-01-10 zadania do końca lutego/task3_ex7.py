print("Witaj drogi użytkowniku!")
print()

# Definiujemy listę imion
names = ["Bogumiła", "Czesław", "Dąbrówka", "Eustachy", "Felicja", "Gniewomir"]

'''
Filtrujemy imiona:
-funkcja lambda sprawdza czy długość imienia jest większa niż 5 znaków
-funkcja filter przetwarza każdy element listy 'names' za pomocą funkcji lambda
-wynik działania funkcji 'filter' zapisujemy jako listę o nazwie 'filtered_names' 
'''

filtered_names = list(filter(lambda name: len(name) > 5, names))

# Wyświetlamy przefiltrowaną listę
print("Imiona z więcej niż 5 znakami:", filtered_names)

print()
print("Do zobaczenia!")