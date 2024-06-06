from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

vegWeb = 'https://www.realcanadiansuperstore.ca/food/fruits-vegetables/fresh-vegetables/c/28195'

path = r"C:\Users\mrina\Documents\SFU\Summer '24\AI4Good\Project\Scraping\chromedriver.exe"
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

driver.get(vegWeb)
vegetables = driver.find_elements(By.XPATH, "//div[contains(@class, 'css-qoklea')]")

for product in vegetables:
    try:
        #name = product.find_element(By.XPATH, ".//div[contains(@class, 'css-8atqhb')]").text
        heading = product.find_element(By.XPATH, ".//h3[contains(@class, 'chakra-heading css-6qrhwc')]").text
        description = product.find_element(By.XPATH, ".//p[contains(@class, 'chakra-text css-1yftjin')]").text
        print(f"Heading: {heading}, Description: {description}")
    except Exception as e:
        print(f"Error extracting product details: {e}")

driver.quit()





