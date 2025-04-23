from selenium import webdriver
from selenium.webdriver.common.by import By

# Specify the path to the ChromeDriver executable
driver = webdriver.Chrome() #executable_path='C:\\Users\\rafal.pieczka\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'
driver.get('https://www.nasa.gov')
headlines = driver.find_elements(By.CLASS_NAME, "headline")
for headline in headlines:
    print(headline.text.strip())
driver.close()