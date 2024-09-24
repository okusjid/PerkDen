from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Utils for managing driver
from utils import initialize_webdriver, load_url, parse_page_source, close_driver

data = []

# Initialize the webdriver
driver = initialize_webdriver()

# Load the target URL
load_url(driver, "https://www.mcbislamicbank.com/personal/digital-banking/mib-debit-card/discount-partners/")

try:
    # Wait until the list of discount partner elements is loaded
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/section[3]/div/div/ol'))
    )
    
    # Find all discount partner containers (adjust XPath based on actual structure)
    discount_partner_elements = driver.find_elements(By.XPATH, '/html/body/section[3]/div/div/ol/div/div')


    # Iterate over each discount partner element
    for partner_element in discount_partner_elements:
        # Extract the image (logo) URL if present
        image_element = partner_element.find_element(By.XPATH, '/html/body/section[3]/div/div/ol/div[1]/div[1]/div/div/div/div/div/div/a/img')
        logo_url = image_element.get_attribute('src')

        # Click the partner to reveal the detailed info (using click event)
        image_element.click()

        # Wait for the detailed popup to appear
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="popmake-11191"]'))
        )
        soup = parse_page_source(driver)
        # Extract the discount partner name and location
        discount_paragraph = soup.find('p', text=lambda x: x and "Discount:" in x)
        if discount_paragraph:
            discount_partner_name = discount_paragraph.find_next('span').get_text(strip=True)
        else:
            discount_partner_name = None

        location_paragraph = soup.find('p', text=lambda x: x and "Location:" in x)
        if location_paragraph:
            discount_partner_location = location_paragraph.find_next('span').get_text(strip=True)
        else:
            discount_partner_location = None



        # Append the data to the list
        data.append({
            'logo_url': logo_url,
            'discount_partner': discount_partner_name,
            'location': discount_partner_location
        })

        print(data)

        # Close the popup if necessary (or navigate back)
        close_button = driver.find_element(By.XPATH, '//*[@id="popmake-11191"]/div/div[4]/div[1]/button')
        close_button.click()

        # Wait briefly before moving to the next iteration to allow the page to refresh
        time.sleep(1)

    # Print the collected data
    print(data)

finally:
    # Wait for a while before closing (adjust as per requirement)
    time.sleep(5)

    # Close the driver once done
    close_driver(driver)
