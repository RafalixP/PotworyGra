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
        name_element = driver.find_element(By.CSS_SELECTOR, 'span.product-name-selector')
        product_name = name_element.text.strip()
    except:
        product_name = "N/A"
    
    try:
        id_element = driver.find_element(By.CSS_SELECTOR, 'span.product-id-selector')
        product_id = id_element.text.strip()
    except:
        product_id = "N/A"
    
    try:
        description_element = driver.find_element(By.CSS_SELECTOR, 'div.product-description-selector')
        description = description_element.text.strip()
    except:
        description = "N/A"
    
    try:
        webpage_element = driver.find_element(By.CSS_SELECTOR, 'a.product-webpage-selector')
        product_webpage = webpage_element.get_attribute('href')
    except:
        product_webpage = url
    
    # Close the WebDriver
    driver.quit()
    
    return product_name, product_id, description, product_webpage