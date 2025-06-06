import sqlite3
from prettytable import PrettyTable

def access_database():
    # Connect to the database
    conn = sqlite3.connect('DCsentry/products.db')

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Example query: Select all rows from the products table
    #cursor.execute('SELECT * FROM price_history')
    cursor.execute('SELECT * FROM products')

    # Fetch all results from the executed query
    products = cursor.fetchall()

    # Get column names
    column_names = [description[0] for description in cursor.description]

    # Create a PrettyTable object
    table = PrettyTable()
    table.field_names = column_names

    # Add rows to the table
    for product in products:
        table.add_row(product)

    # Print the table
    print(table)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    access_database()