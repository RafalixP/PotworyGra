import sqlite3

def update_price_history_schema():
    """
    Rename the 'price' column to 'regular_price' and add a 'discount_price' column in the price_history table.
    """
    try:
        # Connect to the database
        conn = sqlite3.connect('DCsentry/products.db')  # Use the correct database file
        cursor = conn.cursor()
        
        # Step 1: Create a new table with the updated schema
        cursor.execute('''
            CREATE TABLE price_history_new (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER NOT NULL,
                regular_price TEXT,
                discount_price TEXT,
                date TEXT NOT NULL,
                discount TEXT
            )
        ''')
        
        # Step 2: Copy data from the old table to the new table
        cursor.execute('''
            INSERT INTO price_history_new (id, product_id, regular_price, date, discount)
            SELECT id, product_id, price, date, discount FROM price_history
        ''')
        
        # Step 3: Drop the old table
        cursor.execute('DROP TABLE price_history')
        
        # Step 4: Rename the new table to the original table name
        cursor.execute('ALTER TABLE price_history_new RENAME TO price_history')
        
        # Commit the changes
        conn.commit()
        print("Schema updated successfully: Renamed 'price' to 'regular_price' and added 'discount_price'.")
    
    except sqlite3.Error as e:
        print(f"An error occurred while updating the schema: {e}")
    
    finally:
        # Close the connection
        conn.close()

# Run the schema update
if __name__ == "__main__":
    update_price_history_schema()