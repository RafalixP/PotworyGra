# zmienna = input('')

# print('000')
# print(zmienna)

name = input('twoje imię? ')
color = input('Twój kolor? ')
age = int(input("ile masz lat? "))

print(name, "is", age, 'years old and loves the color', color, ".")
print(name, "is", age, 'years old and loves the color', color, ".", sep=" ")
print(name, "is", age, 'years old and loves the color', color, ".", sep="___")
print(name + "is" + 'years old and loves the color' + color + ".")