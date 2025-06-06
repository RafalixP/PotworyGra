import sqlite3

# Connect to the database
conn = sqlite3.connect('DCsentry/products.db')
cursor = conn.cursor()

# Query the schema of the 'products' table
print("Schema of 'products' table:")
cursor.execute("PRAGMA table_info(products)")
for row in cursor.fetchall():
    print(row)

# Query the schema of the 'price_history' table
print("\nSchema of 'price_history' table:")
cursor.execute("PRAGMA table_info(price_history)")
for row in cursor.fetchall():
    print(row)

# Close the connection
conn.close()