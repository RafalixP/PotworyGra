import schedule
import time
from datetime import datetime
from db_operations import add_price_to_history
from web_scraping import get_product_price

def job():
    conn = sqlite3.connect('DCsentry/products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT product_id, product_webpage FROM products')
    products = cursor.fetchall()
    
    for product_id, url in products:
        price = get_product_price(url)
        if price is not None:
            current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            add_price_to_history(product_id, price, current_date)
    
    conn.close()
    print("Prices updated successfully!")

def start_scheduler():
    schedule.every().tuesday.at("10:00").do(job)
    schedule.every().friday.at("10:00").do(job)
    
    while True:
        schedule.run_pending()
        time.sleep(1)