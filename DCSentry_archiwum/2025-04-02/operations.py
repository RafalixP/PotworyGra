import os
import sqlite3
from datetime import datetime
from tabulate import tabulate
import textwrap
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#from scraping import (fetch_product_info)


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
            discount REAL,
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

def clean_price(price_str):
    """
    Clean the price string and convert it to a float.
    If the input is None or invalid, return None.
    """
    if price_str is None or price_str == 'N/A':
        return None
    try:
        return float(price_str.replace(' zł', '').replace(',', '.').strip())
    except ValueError:
        print(f"Failed to clean price: {price_str}")  # Debugging output
        return None

def get_price_trend(product_id):
    conn = sqlite3.connect('DCsentry/products.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT regular_price, discount_price FROM price_history
        WHERE product_id = ?
        ORDER BY datetime(date) DESC
        LIMIT 10
    ''', (product_id,))
    
    prices = cursor.fetchall()
    conn.close()
    
    cleaned_prices = []
    for regular_price, discount_price in prices:
        # Use the discount price if available, otherwise fall back to the regular price
        price = clean_price(discount_price) if discount_price else clean_price(regular_price)
        if price is not None:
            cleaned_prices.append(price)
    
    print(f"Product ID: {product_id}")
    print(f"Raw prices: {prices}")
    print(f"Cleaned prices: {cleaned_prices}")
    
    if len(cleaned_prices) < 2:
        return "No trend"
    
    latest_price = cleaned_prices[0]
    previous_price = cleaned_prices[1]
    
    price_change = latest_price - previous_price
    
    if price_change > 0:
        return f"Plus {price_change:.2f}"
    elif price_change < 0:
        return f"Minus {abs(price_change):.2f}"
    else:
        return "Price steady"

    

def display_all_products():
    """
    Display all products from the database and return the list of products with their actual IDs.
    Rows are ordered by the percentage of price drop (highest drop first).
    """
    try:
        with sqlite3.connect('DCsentry/products.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM products')
            products = cursor.fetchall()
            
            if products:
                headers = ["Display ID", "Name", "Product ID", "Description", "Webpage", "Price Trend", "Regular Price", "Discount Price", "Change", "Discount"]
                wrapped_products = []
                for idx, p in enumerate(products):
                    product_id = p[2]
                    
                    # Fetch the latest regular price, discount price, and discount
                    cursor.execute('''
                        SELECT regular_price, discount_price, discount, date
                        FROM price_history
                        WHERE product_id = ?
                        ORDER BY datetime(date) DESC
                        LIMIT 2
                    ''', (product_id,))
                    price_data = cursor.fetchall()
                    
                    if len(price_data) > 0:
                        # Fetch and clean the latest and previous prices
                        latest_regular_price = clean_price(price_data[0][0]) if price_data[0][0] else None
                        latest_discount_price = clean_price(price_data[0][1]) if price_data[0][1] else None
                        discount = price_data[0][2] if price_data[0][2] else "N/A"
                        previous_price = clean_price(price_data[1][0]) if len(price_data) > 1 and price_data[1][0] else None
                        
                        # Use the discount price if available, otherwise use the regular price
                        latest_price = latest_discount_price if latest_discount_price else latest_regular_price
                        
                        # Debugging: Print the fetched prices
                        print(f"Product ID: {product_id}")
                        print(f"Latest Regular Price: {latest_regular_price}")
                        print(f"Latest Discount Price: {latest_discount_price}")
                        print(f"Previous Price: {previous_price}")
                        
                        # Calculate the percentage of price change
                        if previous_price and latest_price:
                            price_change_percentage = int(((latest_price - previous_price) / previous_price) * 100)
                        else:
                            price_change_percentage = 0  # No change or insufficient data
                        
                        # Debugging: Print the calculated percentage change
                        print(f"Price Change Percentage: {price_change_percentage}%")
                    else:
                        latest_regular_price, latest_discount_price, discount, price_change_percentage = "N/A", "N/A", "N/A", 0
                    
                    wrapped_products.append((
                        f"{idx + 1:<5}",  # Format Display ID to have a width of 5 characters
                        wrap_text(p[1], width=20),  # Adjust column width for Name
                        wrap_text(p[2], width=15),  # Adjust column width for Product ID
                        wrap_text(p[3], width=30),  # Adjust column width for Description
                        wrap_text(p[4], width=40),  # Adjust column width for Webpage
                        get_price_trend(product_id),
                        latest_regular_price,
                        latest_discount_price,
                        f"{price_change_percentage}%",  # Format the percentage change as an integer
                        discount  # Keep Discount column unchanged
                    ))
                
                # Sort the rows by percentage of price drop (negative values first, sorted in descending order)
                wrapped_products.sort(key=lambda x: (int(x[8].replace('%', '')) >= 0, int(x[8].replace('%', ''))), reverse=False)
                
                print("\nAll Products:\n")
                print(tabulate(wrapped_products, headers, tablefmt="grid"))
                return products
            else:
                print("\n---No products found in the database---\n")
                return []
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return []

def get_latest_price(product_id):
    """
    Fetch the latest regular price for a given product ID from the price_history table.
    """
    conn = sqlite3.connect('DCsentry/products.db')
    cursor = conn.cursor()
    
    # Query the regular_price column instead of the old price column
    cursor.execute('''
        SELECT regular_price FROM price_history
        WHERE product_id = ?
        ORDER BY datetime(date) DESC
        LIMIT 1
    ''', (product_id,))
    
    result = cursor.fetchone()
    conn.close()
    
    if result:
        price_str = result[0]
        print(f"Fetched regular price for product {product_id}: {price_str}")  # Debugging statement
        try:
            # Clean the price string
            price_str = price_str.replace(' zł', '').replace(',', '.').strip()
            price = float(price_str)
            return f"{price:.2f} zł"
        except ValueError:
            return "Invalid price"
    return "No price"

def get_latest_discount(product_id):
    conn = sqlite3.connect('DCsentry/products.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT discount FROM price_history
        WHERE product_id = ?
        ORDER BY datetime(date) DESC
        LIMIT 1
    ''', (product_id,))
    
    result = cursor.fetchone()
    conn.close()
    
    if result and result[0] is not None:
        discount = result[0]
        if isinstance(discount, str):
            if '%' in discount:
                return discount
            else:
                return discount
        elif isinstance(discount, (int, float)):
            return f"{discount}% off"
    return "No discount"

def show_all_products():
    """
    Display all products from the database and provide options to modify, add, or remove products.
    """
    while True:
        products = display_all_products()
        
        print("\nOptions:")
        print("1. Modify one of the existing products")
        print("2. Add a new product manually")
        print("3. Add a new product automatically")
        print("4. Remove one of the existing products")
        print("5. Go back to the main screen")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            modify_product(products)
        elif choice == '2':
            add_product(manual=True)
        elif choice == '3':
            add_product(manual=False)
        elif choice == '4':
            remove_product(products)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please select a valid option.")

            
def remove_product(products):
    if not products:
        print("No products available to remove.")
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


def modify_product(products):
    if not products:
        print("No products available to modify.")
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
        cursor.execute('SELECT id, product_id, regular_price, discount_price, date FROM price_history')
        price_history = cursor.fetchall()
        
        if price_history:
            headers = ["ID", "Product ID", "Regular Price", "Discount Price", "Date"]
            wrapped_price_history = [
                (
                    p[0], 
                    p[1], 
                    p[2], 
                    p[3], 
                    p[4]
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
    price_input = input("Enter the regular price: ").replace(',', '.')
    
    # Convert price to float and handle invalid input
    try:
        regular_price = float(price_input)
    except ValueError:
        print("Invalid price value. Please enter a valid number.")
        return
    
    discount_input = input("Enter the discount percentage (leave blank if none): ").strip()
    if discount_input:
        try:
            discount_percentage = float(discount_input.replace('%', '').strip())
            discount_price = regular_price * (1 - discount_percentage / 100)
        except ValueError:
            print("Invalid discount value. Please enter a valid percentage.")
            return
    else:
        discount_price = None
    
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute('''
        INSERT INTO price_history (product_id, regular_price, discount_price, date, discount)
        VALUES (?, ?, ?, ?, ?)
    ''', (product_id, f"{regular_price:.2f} zł", f"{discount_price:.2f} zł" if discount_price else None, current_date, discount_input))
    
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

def fetch_product_info(url):
    """
    Fetch product information (price and discount) from the given URL using web scraping with Selenium.
    """
    # Set up the WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Enable headless mode
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
    driver = webdriver.Chrome(service=Service(), options=options)
    
    # Modify navigator.webdriver to avoid detection
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
        """
    })
    
    # Load the page
    driver.get(url)
    
    # Fetch the price
    try:
        price_element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span.vtmn-font-bold.vtmn-mr-1.vtmn-typo_title-5'))
        )
        price = price_element.text.strip()
        # print(f"Fetched price: {price}")  # Commented out
    except Exception as e:
        price = "N/A"
        # print(f"Failed to fetch price: {e}")  # Commented out
    
    # Fetch the discount code
    try:
        discount_element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span.sticker-item.vtmn-rounded-100'))
        )
        discount_code = discount_element.text.strip()
        # print(f"Fetched discount: {discount_code}")  # Commented out
    except Exception as e:
        discount_code = None
        # print(f"Failed to fetch discount: {e}")  # Commented out
    
    # Close the WebDriver
    driver.quit()
    return price, discount_code

def fetch_price(product_webpage):
    price, discount_code = fetch_product_info(product_webpage)
    return price

def update_all_product_prices():
    """
    Update the prices of all products by fetching the latest information from their respective webpages.
    """
    conn = sqlite3.connect('DCsentry/products.db')  # Ensure the correct database file is used
    cursor = conn.cursor()
    
    # Fetch product_id, product_name, and product_webpage from the database
    cursor.execute('SELECT product_id, product_name, product_webpage FROM products')
    products = cursor.fetchall()
    
    success_count = 0
    failure_count = 0
    
    for product_id, product_name, product_webpage in products:
        # Fetch price and discount code
        price, discount_code = fetch_product_info(product_webpage)
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if price != "N/A":
            # Store the regular price with the currency mark
            regular_price = price
            
            # Calculate the discounted price if a discount is available
            if discount_code and "%" in discount_code:
                try:
                    discount_percentage = float(discount_code.split('%')[0].replace('-', '').strip())
                    discount_price = float(price.replace(',', '.').replace(' zł', '')) * (1 - discount_percentage / 100)
                    discount_price = f"{discount_price:.2f} zł"  # Format with currency
                except ValueError:
                    discount_price = None  # Fallback to no discount
            else:
                discount_price = None  # No discount available
            
            # Successful update
            success_count += 1
            cursor.execute('''
                INSERT INTO price_history (product_id, regular_price, discount_price, date, discount)
                VALUES (?, ?, ?, ?, ?)
            ''', (product_id, regular_price, discount_price, current_date, discount_code))
            print(f"Product ID: {product_id}")
            print(f"Product Name: {product_name}")
            print(f"Regular price: {regular_price}")
            print(f"Discount price: {discount_price if discount_price else 'NULL'}")
        else:
            # Failed update
            failure_count += 1
            print(f"Failed to fetch price and discount for Product ID: {product_id}, Name: {product_name}.")
    
    conn.commit()
    conn.close()
    
    # Print summary
    print(f"Prices updated successfully for {success_count} products.")
    if failure_count > 0:
        print(f"Failed to update prices for {failure_count} products.")

#This function updates the price and discount information for a specific product.
def update_product_info(product_id, url):
    price, discount_code = fetch_product_info(url)
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    conn = sqlite3.connect('DCsentry/products.db')
    cursor = conn.cursor()
    
    # Calculate the discounted price if a discount is available
    if discount_code and "%" in discount_code:
        try:
            discount_percentage = float(discount_code.split('%')[0].replace('-', '').strip())
            discount_price = float(price.replace(',', '.').replace(' zł', '')) * (1 - discount_percentage / 100)
            discount_price = f"{discount_price:.2f} zł"  # Format with currency
        except ValueError:
            discount_price = None  # Fallback to no discount
    else:
        discount_price = None  # No discount available
    
    cursor.execute('''
        INSERT INTO price_history (product_id, regular_price, discount_price, date, discount)
        VALUES (?, ?, ?, ?, ?)
    ''', (product_id, price, discount_price, current_date, discount_code))
    
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
def add_product(manual=True):
    conn = sqlite3.connect('DCsentry/products.db')
    cursor = conn.cursor()
    
    if manual:
        product_name = input("Enter the product name: ")
        product_id = input("Enter the product ID: ")
        description = input("Enter the product description: ")
        product_webpage = input("Enter the product webpage: ")
    else:
        url = input("Enter the product URL: ")
        product_name, product_id, description, product_webpage, price, discount = fetch_product_info(url)
        if not product_name or not product_id or not description:
            print("Failed to fetch product information.")
            return
    
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute('''
        INSERT INTO products (product_name, product_id, description, product_webpage, current_date)
        VALUES (?, ?, ?, ?, ?)
    ''', (product_name, product_id, description, product_webpage, current_date))
    
    if not manual:
        cursor.execute('''
            INSERT INTO price_history (product_id, price, date, discount)
            VALUES (?, ?, ?, ?)
        ''', (product_id, price, current_date, discount))
    
    conn.commit()
    conn.close()
    print(f"Product '{product_name}' added successfully!\n")