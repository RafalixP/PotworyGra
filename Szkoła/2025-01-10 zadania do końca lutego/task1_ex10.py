print('Program oblicza ciąg liczb wg wzoru n**2 - 1/2 wykorzystując podane przez użytkownika wartości początkową (x) i końcową (y)')
print()

x = int(input("Podaj wartość początkową x: "))
y = int(input("Podaj wartość końcową y: "))

# Generowanie i wyświetlanie sekwencji
print("Sekwencja liczb to:")
for n in range(x, y + 1):
    result = n**2 - 1/2
    print(result)