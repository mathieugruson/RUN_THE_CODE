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

button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tarteaucitronAllDenied2"))) # replace with the ID of the button element
button.click()

# Get all <p> tags in the page that contain the Euro symbol
p_tags = [p for p in soup.find_all('p') if '€' in p.get_text()]

# Get all <span> tags with class="tag"
s_tags = [s for s in soup.find_all('span', {'class': 'tag'})]

button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "DataTables_Table_0_next"))) # replace with the ID of the button element
button.click()

# Write to CSV
with open('output1.csv', mode='w') as output_file:
    output_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    output_writer.writerow(['theme', 'montant'])

    # Iterate through pairs of p_tags and s_tags.
    for p, s in zip(p_tags, s_tags):
        output_writer.writerow([s.get_text(), p.get_text()])

# Close the brow
driver.quit()