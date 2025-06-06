def convert_third_char_to_dollar():
    print('Dzień dobry')
    print()

    # Poproś użytkownika o ciąg znaków
    user_string = input("Wprowadź ciąg znaków: ")
    
    # Przekształć co trzeci znak na znak dolara
    result = ""  # pusty string do którego będziemy dopisywać kolejne sprawdzane znaki lub znak dolara zależnie tego czy spelniiony jest warunek
    for i in range(len(user_string)):
        if (i + 1) % 3 == 0:
            result += "$"  # w tym przypadku dopisujemy znak dolara
        else:
            result += user_string[i] # w tym przypadku dopisujemy taką literę jaka była w oryginalnym stringu
    
    return result

# Wywołaj funkcję i wyświetl wynik
print("Przekształcony ciąg znaków to:", convert_third_char_to_dollar())