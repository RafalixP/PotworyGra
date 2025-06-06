import os
import sqlite3


# Function to initialize the database and create the table
def initialize_db():
    db_path = 'DCsentry/products.db'
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create products table without the price column
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
    
    # Create price_history table
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

# Function to add a product to the database
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



# **Function to modify price information**
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
    
    # Display updated price history
    show_price_information()

# **Function to filter specific products**
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