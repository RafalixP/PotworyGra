import os
from operations import (
    initialize_db, show_all_products, display_all_products, show_price_information, 
    add_product, remove_product, modify_product, 
    add_price_information, remove_price_information, modify_price_information,
    update_all_product_prices, fetch_product_info, filter_specific_products
)

# Function to display the main menu
def display_menu():
    print()
    print("Welcome to the DC Sentry app")
    print()
    print("--- What do you want to do? ---")
    print()
    print("1. Show all products")
    print("2. Show price information")
    print("3. Set email address")
    print("4. Send email update")
    print("5. Set the frequency of updates")
    print("6. Exit")

def handle_choice(choice):
    if choice == '1':
        show_all_products()
    elif choice == '2':
        show_price_information()
    elif choice == '3':
        print("You selected: Set email address")
    elif choice == '4':
        print("You selected: Send email update")
    elif choice == '5':
        print("You selected: Set the frequency of updates")
    elif choice == '6':
        print("Exiting the app. Goodbye!")
    else:
        print("Invalid choice. Please select a valid option.")

def main():
    initialize_db()
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '6':
            handle_choice(choice)
            break
        handle_choice(choice)

if __name__ == "__main__":
    main()