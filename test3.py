import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the web page
url = 'https://www.amf-france.org/fr/sanction-transaction/Decisions-de-la-commission-des-sanctions'
driver.get(url)

# Wait for the dynamic content to load
time.sleep(10)

# Get the HTML content of the page after dynamic content has loaded
html = driver.page_source

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all <p> tags in the page
p_tags = soup.find_all('p')

# Print the text content of each <p> tag
for p in p_tags:
    print(p.get_text())

# Close the browser
driver.quit()
