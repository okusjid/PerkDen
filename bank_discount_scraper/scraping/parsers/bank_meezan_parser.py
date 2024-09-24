# //*[@id="app"]/div/main/div/div[4]/div/div[2]/div/div[2]
# //*[@id="app"]/div/main/div[2]/div[1]/div/div/div/a/div[1]
# //*[@id="card-deals"]/div/div

# //*[@id="app"]/div/main/div/div[5]/div[2]/div[1]/div
# //*[@id="app"]/div/main/div[2]/div[1]/div/div/div/a/div[1]
# //*[@id="card-deals"]/div/div

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

from utils import initialize_webdriver, load_url, parse_page_source, close_driver

driver = initialize_webdriver()
# Wait for the page to load
load_url(driver, "https://www.meezanbank.com/card-discounts/")
soup = parse_page_source(driver)

# Wait for the specific element to be present
element1 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div[4]/div/div[2]/div/div[2]'))
)

#element2 = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div[2]/div[1]/div/div/div/a/div[1]')
#element3 = driver.find_element(By.XPATH, '//*[@id="card-deals"]/div/div')

# Extract the HTML content from the elements
html_content1 = element1.get_attribute('outerHTML')


# Now use BeautifulSoup to parse the extracted HTML content
soup1 = BeautifulSoup(html_content1, 'html.parser')


# Example of extracting data using BeautifulSoup
# You can modify this part to extract specific data, like text, links, or attributes

# Extract text from soup
text1 = soup1.get_text().strip()


# Print out or store the scraped data
print("Element 1 content: ", text1)


# Close the Selenium browser once scraping is done
close_driver(driver)