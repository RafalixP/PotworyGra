# Lista imion
names = ["Kacper", "Pawel", "Patryk"]

# Tworzymy plik i zapisujemy imiona, każde w nowej linii
with open('names.txt', 'w') as f:
    for name in names:
        f.write("\n")  # Pusta linia
        f.write(f"{name}\n")  # Imię w nowej linii

# Sprawdzamy zawartość pliku
with open('names.txt', 'r') as f:
    content = f.read()

print(content)