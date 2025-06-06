import sqlite3
from datetime import datetime
from tabulate import tabulate

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
    
    conn.close()

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

def modify_price_information():
    conn = sqlite3.connect('DCsentry/products.db')
    cursor = conn.cursor()

    price_id = input("Enter the ID of the price information you want to modify: ")

    cursor.execute('SELECT * FROM price_history WHERE id = ?', (price_id,))
    price_info = cursor.fetchone()

    if price_info:
        print("\nCurrent price information details:")
        print(f"ID: {price_info[0]}")
        print(f"Product ID: {price_info[1]}")
        print(f"Price: {price_info[2]}")
        print(f"Date: {price_info[3]}\n")
        
        new_price = input(f"Enter new price (leave blank to keep '{price_info[2]}'): ").replace(',', '.')
        
        try:
            new_price = float(new_price)
        except ValueError:
            print("Invalid price value. Please enter a valid number.")
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