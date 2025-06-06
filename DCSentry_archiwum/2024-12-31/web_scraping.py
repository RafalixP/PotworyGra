import requests
from bs4 import BeautifulSoup

def get_product_price(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    price_tag = soup.find('span', class_='price')
    if price_tag:
        price = price_tag.text.strip()
        return float(price.replace(',', '').replace('$', ''))  # Adjust as needed
    return None