import os
import sqlite3
from datetime import datetime
from tabulate import tabulate
import textwrap
import requests
from bs4 import BeautifulSoup


def initialize_db():
    db_path = 'DCsentry/products.db'
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            product_id TEXT NOT NULL,
            description TEXT,
            product_webpage TEXT NOT NULL,
            current_date TEXT NOT NULL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS price_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id TEXT NOT NULL,
            price REAL NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database initialized and tables created (if they didn't exist).")

def wrap_text(s, width=30):
    if s is None:
        return ""
    if isinstance(s, str):
        return "\n".join(textwrap.wrap(s, width))
    return s

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
def display_all_products():
    """
    Display all products from the database and return the list of products with their actual IDs.
    """
    try:
        with sqlite3.connect('DCsentry/products.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM products')
            products = cursor.fetchall()
            
            if products:
                headers = ["Display ID", "Name", "Product ID", "Description", "Webpage", "Date", "Price Trend"]
                wrapped_products = [
                    (
                        idx + 1,  # Generate new display ID starting from 1
                        wrap_text(p[1]), 
                        p[2], 
                        wrap_text(p[3]), 
                        wrap_text(p[4]), 
                        p[5],
                        get_price_trend(p[2])
                    ) for idx, p in enumerate(products)
                ]
                print("\nAll Products:\n")
                print(tabulate(wrapped_products, headers, tablefmt="grid"))
                return products
            else:
                print("\n---No products found in the database---\n")
                return []
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return []

def show_all_products():
    """
    Display all products from the database and provide options to modify, add, or remove products.
    """
    while True:
        products = display_all_products()
        
        print("\nOptions:")
        print("1. Modify one of the existing products")
        print("2. Add a new product")
        print("3. Remove one of the existing products")
        print("4. Go back to the main screen")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            modify_product(products)
        elif choice == '2':
            add_product()
        elif choice == '3':
            remove_product(products)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")

def remove_product():
    products = display_all_products()  # Display all products before removing
    if not products:
        return
    
    display_id = input("Enter the display ID of the product you want to remove: ")
    
    try:
        display_id = int(display_id)
        if display_id < 1 or display_id > len(products):
            raise ValueError("Invalid display ID.")
    except ValueError as e:
        print(e)
        return
    
    actual_id = products[display_id - 1][0]
    
    conn = sqlite3.connect('DCsentry/products.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM products WHERE id = ?', (actual_id,))
    product = cursor.fetchone()
    
    if product:
        cursor.execute('DELETE FROM products WHERE id = ?', (actual_id,))
        conn.commit()
        print(f"Product ID {actual_id} removed successfully!\n")
        
        cursor.execute('DELETE FROM price_history WHERE product_id = ?', (product[2],))
        conn.commit()
        
    else:
        print(f"No product found with ID {actual_id}.\n")
    
    conn.close()
    #show_all_products()

def modify_product():
    products = display_all_products()  # Display all products before modifying
    if not products:
        return
    
    display_id = input("Enter the display ID of the product you want to modify: ")
    
    try:
        display_id = int(display_id)
        if display_id < 1 or display_id > len(products):
            raise ValueError("Invalid display ID.")
    except ValueError as e:
        print(e)
        return
    
    actual_id = products[display_id - 1][0]
    
    conn = sqlite3.connect('DCsentry/products.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM products WHERE id = ?', (actual_id,))
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
        ''', (new_name, new_product_id, new_description, new_webpage, actual_id))
        
        conn.commit()
        print(f"Product ID {actual_id} updated successfully!\n")
    else:
        print(f"No product found with ID {actual_id}.\n")
    
    conn.close()
#    show_all_products()


def show_price_information():
    def display_price_history():
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
    
    conn = sqlite3.connect('DCsentry/products.db')
    cursor = conn.cursor()
    
    while True:
        display_price_history()
        
        print("\nOptions:")
        print("1. Automatically check all prices")
        print("2. Add price information for specific products")
        print("3. Remove price information for specific products")
        print("4. Modify price information for specific products")
        print("5. Filter specific products")
        print("6. Go back to the main screen")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            update_all_product_prices()
        elif choice == '2':
            add_price_information()
        elif choice == '3':
            remove_price_information()
        elif choice == '4':
            modify_price_information()
        elif choice == '5':
            filter_specific_products()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please select a valid option.")
    
    conn.close()

# **Function to add price information**
def add_price_information():
    conn = sqlite3.connect('DCsentry/products.db')
    cursor = conn.cursor()

    # Display available products
    products = display_all_products()
    if not products:
        return
    
    display_id = input("\nEnter the display ID of the product: ")
    
    try:
        display_id = int(display_id)
        if display_id < 1 or display_id > len(products):
            raise ValueError("Invalid display ID.")
    except ValueError as e:
        print(e)
        return
    
    actual_id = products[display_id - 1][0]
    product_id = products[display_id - 1][2]
    
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
    print()
    print(f"Price information for product ID {product_id} added successfully!\n")

#This function removes price information from the price_history table based on the provided ID
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

def modify_price_information():
    conn = sqlite3.connect('DCsentry/products.db')
    cursor = conn.cursor()

    # Display available price information
    cursor.execute('SELECT * FROM price_history')
    price_history = cursor.fetchall()
    
    if price_history:
        headers = ["Display ID", "Product ID", "Price", "Date"]
        print("\nAvailable Price Information:\n")
        print(tabulate(price_history, headers, tablefmt="grid"))
    else:
        print("\nNo price information found in the database.\n")
        conn.close()
        return
    
    price_id = input("Enter the ID of the price information you want to modify: ")
    
    cursor.execute('SELECT * FROM price_history WHERE id = ?', (price_id,))
    price_info = cursor.fetchone()
    
    if price_info:
        print("\nCurrent price information details:")
        print(f"ID: {price_info[0]}")
        print(f"Product ID: {price_info[1]}")
        print(f"Price: {price_info[2]}")
        print(f"Date: {price_info[3]}\n")
        
        new_price_input = input(f"Enter new price (leave blank to keep '{price_info[2]}'): ").replace(',', '.') or price_info[2]
        
        try:
            new_price = float(new_price_input)
        except ValueError:
            print("Invalid price value. Please enter a valid number.")
            conn.close()
            return
        
        cursor.execute('''
            UPDATE price_history
            SET price = ?
            WHERE id = ?
        ''', (new_price, price_id))
        
        conn.commit()
        print(f"Price information ID {price_id} updated successfully!\n")
    else:
        print(f"No price information found with ID {price_id}.\n")
    
    conn.close()


#This function updates the prices of all products by fetching the latest information from their respective webpages.

def update_all_product_prices():
    conn = sqlite3.connect('DCsentry/products.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT product_id, product_webpage FROM products')
    products = cursor.fetchall()
    
    for product_id, product_webpage in products:
        update_product_info(product_id, product_webpage)
    
    conn.close()
    print("All product prices updated successfully!\n")


#This function fetches product information from a given URL using web scraping.
def fetch_product_info(url):
    """
    Fetch product information from the given URL using web scraping.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Debugging: Print the full HTML content
    print(soup.prettify())
    
    # Use the specific class name for the price element, navigating through parent elements
    price_section = soup.select_one('div.price-section.svelte-nkher4.regular')
    price_element = None
    if price_section:
        price_wrapper = price_section.select_one('div.price-wrapper.vtmn-flex.vtmn-flex-wrap.vtmn-items-center.svelte-1e1jymn')
        if price_wrapper:
            price_element = price_wrapper.select_one('span.vtmn-font-bold.vtmn-mr-1.vtmn-typo_title-5.svelte-1e1jymn')
    
    discount_code_element = soup.select_one('.discount-code')
    
    # Debugging: Print the selected elements
    print(f"Price element: {price_element}")
    print(f"Discount code element: {discount_code_element}")
    
    price = price_element.text.strip() if price_element else "N/A"
    discount_code = discount_code_element.text.strip() if discount_code_element else None
    
    return price, discount_code



def update_all_product_prices():
    """
    Update the prices of all products by fetching the latest information from their respective webpages.
    """
    conn = sqlite3.connect('DCsentry/products.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT product_id, product_webpage FROM products')
    products = cursor.fetchall()
    
    for product_id, product_webpage in products:
        price, discount_code = fetch_product_info(product_webpage)
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        cursor.execute('''
            INSERT INTO price_history (product_id, price, date)
            VALUES (?, ?, ?)
        ''', (product_id, price, current_date))
        
        if discount_code:
            cursor.execute('''
                INSERT INTO discount_codes (product_id, discount_code, date)
                VALUES (?, ?, ?)
            ''', (product_id, discount_code, current_date))
    
    conn.commit()
    conn.close()
    print("All product prices updated successfully!\n")


#This function updates the price and discount information for a specific product.
def update_product_info(product_id, url):
    price, discount_code = fetch_product_info(url)
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    conn = sqlite3.connect('DCsentry/products.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO price_history (product_id, price, date)
        VALUES (?, ?, ?)
    ''', (product_id, price, current_date))
    
    if discount_code:
        cursor.execute('''
            INSERT INTO discount_codes (product_id, discount_code, date)
            VALUES (?, ?, ?)
        ''', (product_id, discount_code, current_date))
    
    conn.commit()
    conn.close()
    print(f"Price and discount information for product ID {product_id} updated successfully!\n")


#This function filters and displays price history for a specific product based on user input.
def filter_specific_products():
    conn = sqlite3.connect('DCsentry/products.db')
    cursor = conn.cursor()

    cursor.execute('SELECT product_id, product_name FROM products')
    products = cursor.fetchall()
    
    if products:
        headers = ["Row Number", "Product ID", "Name"]
        products_with_row_numbers = [(i+1, p[0], p[1]) for i, p in enumerate(products)]
        print("\nAvailable Products:\n")
        print(tabulate(products_with_row_numbers, headers, tablefmt="grid"))
    
    row_number = input("\nEnter the row number to filter: ")
    
    try:
        row_number = int(row_number)
        if row_number < 1 or row_number > len(products):
            raise ValueError("Invalid row number.")
    except ValueError as e:
        print(e)
        return

    product_id = products[row_number - 1][0]

    cursor.execute('SELECT * FROM price_history WHERE product_id = ?', (product_id,))
    price_history = cursor.fetchall()

    if price_history:
        headers = ["Display  ID", "Product ID", "Price", "Date"]
        wrapped_price_history = [
            (
                p[0], 
                p[1], 
                p[2], 
                p[3]
            ) for p in price_history
        ]
        print("\nFiltered Price History:\n")
        print(tabulate(wrapped_price_history, headers, tablefmt="grid"))
    else:
        print(f"\nNo price information found for product ID {product_id}.\n")
    
    conn.close()


#This function adds a new product to the products table.
def add_product():
    conn = sqlite3.connect('DCsentry/products.db')
    cursor = conn.cursor()
    
    product_name = input("Enter the product name: ")
    product_id = input("Enter the product ID: ")
    description = input("Enter the product description: ")
    product_webpage = input("Enter the product webpage: ")
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute('''
        INSERT INTO products (product_name, product_id, description, product_webpage, current_date)
        VALUES (?, ?, ?, ?, ?)
    ''', (product_name, product_id, description, product_webpage, current_date))
    
    conn.commit()
    conn.close()
    print(f"Product '{product_name}' added successfully!\n")