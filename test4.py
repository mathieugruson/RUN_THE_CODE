import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the first page of the web page
url = 'https://www.amf-france.org/fr/sanction-transaction/Decisions-de-la-commission-des-sanctions'
driver.get(url)

# Wait for the dynamic content to load
time.sleep(10)

# Extract the HTML content of the page after dynamic content has loaded
html = driver.page_source

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Loop over all page numbers and extract the content from each page
# Loop through all pages and extract the desired <p> tags
while True:
    # Wait for the dynamic content to load
    time.sleep(10)

    # Extract the HTML content of the page after dynamic content has loaded
    html = driver.page_source

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all <p> tags in the page that contain the Euro symbol
    p_tags = [p for p in soup.find_all('p') if '€' in p.get_text()]

    # Print the text content of each <p> tag
    for p in p_tags:
        print(p.get_text())

    # Check if there is a link to the next page
     next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="DataTables_Table_0_next"]')))
    if not next_button:
        break

    # Navigate to the next page
    current_page += 1
    next_button.click()

# Close the browser
driver.quit()
