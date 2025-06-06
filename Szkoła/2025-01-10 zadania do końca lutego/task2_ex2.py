def compare_strings():
    print('Dzień dobry')
    print()
    # poproś użytkownika o dwa ciągi znaków
    string1 = input("Wprowadź pierwszy ciąg znaków: ")
    string2 = input("Wprowadź drugi ciąg znaków: ")
    
    # porównanie długości ciągów znaków
    if len(string1) > len(string2):
        return string1
    elif len(string2) > len(string1):
        return string2
    else:
        return "Oba ciągi znaków mają równą długość."

#wynik
print("Dłuższy ciąg znaków to:", compare_strings())