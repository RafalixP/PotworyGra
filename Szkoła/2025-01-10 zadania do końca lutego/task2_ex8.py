import random
import string

# funkcja generująca hasło
def generate_password():
    # wymagania które powinno spełniać hasło
    min_length = 6
    max_length = 24
    length = random.randint(min_length, max_length) #tu losujemy jaką długość będzie miało hasło w granicach określonych przez zmienne min_length oraz max_length
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    special = "!%$#@?"
    all_characters = lower + upper + special
    
    password = ''.join(random.choice(all_characters) for i in range(length))
    # sprawdzenie wymagań odnośnie znaków tworzących hasło
    if (any(c in lower for c in password) and
        any(c in upper for c in password) and
        any(c in special for c in password)):
        return password
    else:
        return generate_password()

def password_creator():
    print("Witaj w programie do generowania haseł!")
    
    while True:
        choice = input("Czy chcesz wygenerować hasło? (t/n): ").lower()
        
        if choice == 'n':
            print("Dziękujemy za skorzystanie z programu. Do zobaczenia!")
            break
        elif choice == 't':
            password = generate_password()
            print(f"Hasło wygenerowane dla Ciebie to: {password}")
        else:
            print("Nieprawidłowy wybór. Proszę wpisać 't' lub 'n'.")

# uruchamiamy program
if __name__ == "__main__":
    password_creator()