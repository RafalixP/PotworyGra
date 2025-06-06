def add_product(manual=True, url=None):
    """
    Add a new product to the database, either manually or automatically by scraping product details.
    
    Parameters:
    manual (bool): If True, prompts the user for product details manually.
    url (str): The URL of the product webpage (used in automatic mode).
    """
    conn = sqlite3.connect('DCsentry/products.db')
    cursor = conn.cursor()
    
    try:
        if manual:
            # Manual mode: Prompt the user for product details
            product_name = input("Enter the product name: ")
            product_id = input("Enter the product ID: ")
            description = input("Enter the product description: ")
            product_webpage = input("Enter the product webpage: ")
            price = input("Enter the product price: ")
            discount = input("Enter the product discount (if any): ")
        else:
            # Automatic mode: Fetch product details from the URL
            if not url:
                url = input("Enter the product URL: ")
            try:
                product_name, product_id, description, product_webpage, price, discount = fetch_product_info(url)
                if not product_name or not product_id or not description:
                    print("Failed to fetch product information. Please check the URL.")
                    return
            except Exception as e:
                print(f"An error occurred while fetching product information: {e}")
                return
        
        # Get the current date and time
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Insert product details into the `products` table
        cursor.execute('''
            INSERT INTO products (product_name, product_id, description, product_webpage, date_added)
            VALUES (?, ?, ?, ?, ?)
        ''', (product_name, product_id, description, product_webpage, current_date))
        
        # Insert price details into the `price_history` table
        try:
            price, discount_code = fetch_product_info(product_webpage)
        except ValueError:
            print(f"Failed to fetch price and discount for: {product_webpage}")
            price, discount_code = "N/A", "N/A"
        
        cursor.execute('''
            INSERT INTO price_history (product_id, regular_price, date, discount)
            VALUES (?, ?, ?, ?)
        ''', (product_id, price, current_date, discount))
        
        conn.commit()
        print(f"Product '{product_name}' added successfully!\n")
    
    except sqlite3.Error as db_error:
        print(f"Database error: {db_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        conn.close()

def fetch_product_info(product_webpage):
    try:
        # Simulate fetching the webpage (replace with your actual logic)
        print(f"Fetching product info for: {product_webpage}")
        
        # Example: Extract price and discount code (replace with actual logic)
        price = "100.00"  # Replace with logic to extract price
        discount_code = "DISCOUNT10"  # Replace with logic to extract discount code

        # Handle missing values
        if not price:
            price = "N/A"
        if not discount_code:
            discount_code = "N/A"

        print(f"Fetched price: {price}, discount code: {discount_code}")
        return price, discount_code
    except Exception as e:
        print(f"Error fetching product info for {product_webpage}: {e}")
        return None, None  # Return default values in case of an error

def update_all_product_prices():
    for product_webpage in product_webpages:
        try:
            price, discount_code = fetch_product_info(product_webpage)
            if price is None or discount_code is None:
                print(f"Failed to fetch price or discount for {product_webpage}")
                price, discount_code = "N/A", "N/A"
            
            # Update the database or perform other actions
            print(f"Price: {price}, Discount Code: {discount_code}")
        except ValueError as e:
            print(f"Error updating product prices: {e}")