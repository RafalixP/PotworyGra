import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#This function fetches product information from a given URL using web scraping.
def fetch_product_info(url):
    """
    Fetch product information from the given URL using web scraping with Selenium.
    """
    # Set up the WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    # Load the page
    driver.get(url)
    
    # Example selectors, adjust based on the actual HTML structure of the product page
    try:
        price_element = driver.find_element(By.CSS_SELECTOR, 'span.product-price-selector')
        price = price_element.text.strip()
    except:
        price = "N/A"
    
    try:
        discount_element = driver.find_element(By.CSS_SELECTOR, 'span.product-discount-selector')
        discount_code = discount_element.text.strip()
    except:
        discount_code = None
    
    # Close the WebDriver
    driver.quit()
    
    return price, discount_code