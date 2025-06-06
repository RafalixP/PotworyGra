import threading
from datetime import datetime
from db_operations import initialize_db
from product_operations import add_product, show_all_products, remove_product, modify_product
from price_history_update import add_price_information, show_price_information, remove_price_information, modify_price_information

def display_menu():
    print()
    print("Welcome to the DC Sentry app")
    print()
    print("1. Add a product")
    print("2. Show all products")
    print("3. Show price information")
    print("4. Set email address")
    print("5. Set the frequency of updates")
    print("6. Send email update")
    print("7. Exit")

def handle_choice(choice):
    if choice == '1':
        add_product()
    elif choice == '2':
        show_all_products()
    elif choice == '3':
        show_price_information()
    elif choice == '4':
        print("You selected: Set email address")
    elif choice == '5':
        print("You selected: Set the frequency of updates")
    elif choice == '6':
        print("You selected: Send email update")
    elif choice == '7':
        print("Exiting the app. Goodbye!")
    else:
        print("Invalid choice. Please select a valid option.")

def main():
    initialize_db()
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '7':
            handle_choice(choice)
            break
        handle_choice(choice)

if __name__ == "__main__":
    main()