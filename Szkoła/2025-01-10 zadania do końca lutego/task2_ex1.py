def main(input_func=input):
    print("Cześć! Wprowadź proszę hasło.")
    print()
    messages = []
    messages.append("")

    # pierwsza próba hasła
    password1 = input_func("Wprowadź hasło: ")

    # druga próba hasła
    password2 = input_func("Powtórz hasło: ")

    # porównanie haseł
    if password1 == password2:
        messages.append("Brawo, hasła są takie same.")
    else:
        messages.append("Błąd: Hasła nie są takie same.")
    
    return "\n".join(messages)

if __name__ == "__main__":
    print(main())