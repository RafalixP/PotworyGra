import sqlite3
from datetime import datetime
from tabulate import tabulate
import textwrap

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

def add_product():
    conn = sqlite3.connect('DCsentry/products.db')
    cursor = conn.cursor()
    
    product_name = input("Enter the product name: ")
    product_id = input("Enter the product ID: ")
    description = input("Enter the product description: ")
    product_webpage = input("Enter the product webpage URL: ")
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute('''
        INSERT INTO products (product_name, product_id, description, product_webpage, current_date)
        VALUES (?, ?, ?, ?, ?)
    ''', (product_name, product_id, description, product_webpage, current_date))
    
    conn.commit()
    conn.close()
    print(f"Product '{product_name}' added successfully!\n")

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

def filter_specific_products():
    conn = sqlite3.connect('DCsentry/products.db')
    cursor = conn.cursor()

    # Display available products with row numbers
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
        headers = ["ID", "Product ID", "Price", "Date"]
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