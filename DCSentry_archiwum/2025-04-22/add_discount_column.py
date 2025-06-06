import sqlite3

def add_discount_column():
    conn = sqlite3.connect('DCsentry/products.db')
    cursor = conn.cursor()
    
    # Add the discount column to the price_history table
    cursor.execute('''
        ALTER TABLE price_history
        ADD COLUMN discount REAL
    ''')
    
    conn.commit()
    conn.close()
    print("Discount column added to price_history table.")

if __name__ == "__main__":
    add_discount_column()