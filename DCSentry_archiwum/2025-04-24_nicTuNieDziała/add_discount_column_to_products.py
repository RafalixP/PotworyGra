import sqlite3

def add_discount_column_to_products():
    conn = sqlite3.connect('DCsentry/products.db')
    cursor = conn.cursor()
    
    # Add the discount column to the products table
    cursor.execute('''
        ALTER TABLE products
        ADD COLUMN latest_discount TEXT
    ''')
    
    conn.commit()
    conn.close()
    print("Discount column added to products table.")

if __name__ == "__main__":
    add_discount_column_to_products()