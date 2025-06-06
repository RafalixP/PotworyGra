import sqlite3
from tabulate import tabulate
import textwrap

# Define a helper function to wrap text:
def wrap_text(s, width=30):
    return "\n".join(textwrap.wrap(s, width))

# Connect to the database
conn = sqlite3.connect('DCsentry/products.db')
cursor = conn.cursor()

# Fetch all products from the database
cursor.execute('SELECT * FROM products')
products = cursor.fetchall()

# Define headers for the products table
product_headers = ["ID", "Name", "Product ID", "Current Price", "Description", "Webpage", "Date"]

# Wrap text in the 'Name', 'Description', and 'Webpage' columns for products
wrapped_products = [
    (
        p[0], 
        wrap_text(p[1]), 
        p[2], 
        p[3], 
        wrap_text(p[4]), 
        wrap_text(p[5]), 
        p[6]
    ) for p in products
]

# Display the products table using tabulate
print("\nProducts Table:\n")
print(tabulate(wrapped_products, product_headers, tablefmt="grid"))

# Fetch all price history from the database
cursor.execute('SELECT * FROM price_history')
price_history = cursor.fetchall()

# Define headers for the price history table
price_history_headers = ["ID", "Product ID", "Price", "Date"]

# Display the price history table using tabulate
print("\nPrice History Table:\n")
print(tabulate(price_history, price_history_headers, tablefmt="grid"))

# Close the database connection
conn.close()