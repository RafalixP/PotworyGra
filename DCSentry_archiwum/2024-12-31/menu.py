import os
import sqlite3
from datetime import datetime
from tabulate import tabulate
import textwrap
from db_operations import initialize_db, add_price_information
from product_operations import add_product, show_all_products, remove_product, modify_product, fetch_product_info, update_product_info, update_all_product_prices, filter_specific_products 
from price_history_update import show_price_information

    # Display updated price history
show_price_information()

# Define a helper function to wrap text:
def wrap_text(s, width=30):
    if s is None:
        return ""
    if isinstance(s, str):
        return "\n".join(textwrap.wrap(s, width))
    return s

# Helper function to determine the price trend:

def get_price_trend(product_id):
    conn = sqlite3.connect('DCsentry/products.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT price FROM price_history
        WHERE product_id = ?
        ORDER BY date DESC
        LIMIT 2
    ''', (product_id,))
    
    prices = cursor.fetchall()
    conn.close()
    
    if len(prices) < 2:
        return "No trend"
    
    latest_price, previous_price = prices[0][0], prices[1][0]
    price_change = latest_price - previous_price
    
    if price_change > 0:
        return f"Price raise by {price_change:.2f}"
    elif price_change < 0:
        return f"Price drop by {abs(price_change):.2f}"
    else:
        return "Price steady"

# Function to show all products in the database
 
def show_all_products():
    conn = sqlite3.connect('DCsentry/products.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    
    if products:
        headers = ["ID", "Name", "Product ID", "Description", "Webpage", "Date", "Price Trend"]
        wrapped_products = [
            (
                p[0], 
                wrap_text(p[1]), 
                p[2], 
                wrap_text(p[3]), 
                wrap_text(p[4]), 
                p[5],
                get_price_trend(p[2])
            ) for p in products
        ]
        print("\nAll Products:\n")
        print(tabulate(wrapped_products, headers, tablefmt="grid"))
        
        while True:
            print("\nOptions:")
            print("1. Modify one of the existing products")
            print("2. Add a new product")
            print("3. Remove one of the existing products")
            print("4. Go back to the main screen")
            
            choice = input("Enter your choice: ").strip()
            
            if choice == '1':
                modify_product()
            elif choice == '2':
                add_product()
            elif choice == '3':
                remove_product()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please select a valid option.")
    else:
        print("\n---No products found in the database---\n")
    
    conn.close()

# Function to remove a product from the database
def remove_product():
    conn = sqlite3.connect('DCsentry/products.db')
    cursor = conn.cursor()
    
    product_id = input("Enter the ID of the product you want to remove: ")
    
    cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
    product = cursor.fetchone()
    
    if product:
        cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
        conn.commit()
        print(f"Product ID {product_id} removed successfully!\n")
        
        # Remove associated price history records
        cursor.execute('DELETE FROM price_history WHERE product_id = ?', (product[2],))
        conn.commit()
        
    else:
        print(f"No product found with ID {product_id}.\n")
    
    conn.close()
    show_all_products()

# Function to modify a product in the database
def modify_product():
    conn = sqlite3.connect('DCsentry/products.db')
    cursor = conn.cursor()
    
    product_id = input("Enter the ID of the product you want to modify: ")
    
    cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
    product = cursor.fetchone()
    
    if product:
        print("\nCurrent product details:")
        print(f"ID: {product[0]}")
        print(f"Name: {product[1]}")
        print(f"Product ID: {product[2]}")
        print(f"Description: {product[3]}")
        print(f"Webpage: {product[4]}")
        print(f"Date: {product[5]}\n")
        
        new_name = input(f"Enter new name (leave blank to keep '{product[1]}'): ") or product[1]
        new_product_id = input(f"Enter new product ID (leave blank to keep '{product[2]}'): ") or product[2]
        
        new_description = input(f"Enter new description (leave blank to keep '{product[3]}'): ") or product[3]
        new_webpage = input(f"Enter new webpage (leave blank to keep '{product[4]}'): ") or product[4]
        
        cursor.execute('''
            UPDATE products
            SET product_name = ?, product_id = ?, description = ?, product_webpage = ?
            WHERE id = ?
        ''', (new_name, new_product_id, new_description, new_webpage, product_id))
        
        conn.commit()
        print(f"Product ID {product_id} updated successfully!\n")
    else:
        print(f"No product found with ID {product_id}.\n")
    
    conn.close()
    show_all_products()

# **Function to show price information in the database**
def show_price_information():
    conn = sqlite3.connect('DCsentry/products.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM price_history')
    price_history = cursor.fetchall()
    
    if price_history:
        headers = ["ID", "Product ID", "Price", "Date"]
        wrapped_price_history = [
            (
                p[0], 
                p[1], 
                p[2], 
                p[3]
            ) for p in price_history
        ]
        print("\nPrice History:\n")
        print(tabulate(wrapped_price_history, headers, tablefmt="grid"))
    else:
        print("\nNo price information found in the database.\n")
    
    while True:
        print("\nOptions:")
        print("1. Add price information for specific products")
        print("2. Remove price information for specific products")
        print("3. Modify price information for specific products")
        print("4. Filter specific products")
        print("5. Go back to the main screen")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            add_price_information()
        elif choice == '2':
            remove_price_information()
        elif choice == '3':
            modify_price_information()
        elif choice == '4':
            filter_specific_products()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please select a valid option.")
    
    conn.close()

# **Function to add price information**
def add_price_information():
    conn = sqlite3.connect('DCsentry/products.db')
    cursor = conn.cursor()

    # Display available products
    cursor.execute('SELECT product_id, product_name FROM products')
    products = cursor.fetchall()
    
    if products:
        headers = ["Product ID", "Name"]
        print("\nAvailable Products:\n")
        print(tabulate(products, headers, tablefmt="grid"))
    
    product_id = input("\nEnter the product ID: ")
    
    # Handle comma as decimal separator
    price_input = input("Enter the price: ").replace(',', '.')
    
    # Convert price to float and handle invalid input
    try:
        price = float(price_input)
    except ValueError:
        print("Invalid price value. Please enter a valid number.")
        return
    
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute('''
        INSERT INTO price_history (product_id, price, date)
        VALUES (?, ?, ?)
    ''', (product_id, price, current_date))
    
    conn.commit()
    conn.close()
    print(f"Price information for product ID {product_id} added successfully!\n")

# **Function to remove price information**
def remove_price_information():
    conn = sqlite3.connect('DCsentry/products.db')
    cursor = conn.cursor()

    price_id = input("Enter the ID of the price information you want to remove: ")

    cursor.execute('SELECT * FROM price_history WHERE id = ?', (price_id,))
    price_info = cursor.fetchone()

    if price_info:
        cursor.execute('DELETE FROM price_history WHERE id = ?', (price_id,))
        conn.commit()
        print(f"Price information ID {price_id} removed successfully!\n")
    else:
        print(f"No price information found with ID {price_id}.\n")
    
    conn.close()
    
    # Display updated price history
    show_price_information()



# Function to display the main menu
def display_menu():
    print()
    print("Welcome to the DC Sentry app")
    print()
    print("1. Show all products")
    print("2. Show price information")
    print("3. Set email address")
    print("4. Set the frequency of updates")
    print("5. Send email update")
    print("6. Exit")

def handle_choice(choice):
    if choice == '1':
        show_all_products()
    elif choice == '2':
        show_price_information()
    elif choice == '3':
        print("You selected: Set email address")
    elif choice == '4':
        print("You selected: Set the frequency of updates")
    elif choice == '5':
        print("You selected: Send email update")
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