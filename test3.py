from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

from selenium import webdriver
import csv  

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

# Get all <p> tags in the page that contain the Euro symbol
p_tags = [p for p in soup.find_all('p') if '€' in p.get_text()]

# Get all <span> tags with class="tag"
s_tags = [s for s in soup.find_all('span', {'class': 'tag'})]

# Write to CSV
with open('output.csv', mode='w') as output_file:
    output_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    output_writer.writerow(['amount', 'theme'])

    # Iterate through pairs of p_tags and s_tags.
    for p, s in zip(p_tags, s_tags):
        output_writer.writerow([p.get_text(), s.get_text()])

# Close the brow