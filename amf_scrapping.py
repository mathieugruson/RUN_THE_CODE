from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import time
import csv
import re
import os

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

# Click the "refuser tout" button to disable cookie consent
button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tarteaucitronAllDenied2")))
button.click()

# Write to CSV
with open('output1.csv', mode='w') as output_file:
    output_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    output_writer.writerow(['date', 'theme', 'montant'])

    # Keep scraping the page until the "next page" button is disabled
    count = 0
    while count < 41:
        # Get all <p> tags in the page that contain the Euro symbol
        p_tags = [p for p in soup.find_all('p') if '€' in p.get_text() or 'euros' in p.get_text()]

        # Get all <span> tags with class="tag"
        s_tags = [s for s in soup.find_all('span', {'class': 'tag'})]

        # Get all <span> tags with class="date"
        d_tags = [d for d in soup.find_all('span', {'class': 'date'})]

        # Write the data to the CSV file
        for p, s, d in zip(p_tags, s_tags, d_tags):
            year = d.get_text().split()[-1]  # Extract the last word of the date string
            output_writer.writerow([year, s.get_text(), p.get_text()])
        # Click the "next page" button if it's clickable, otherwise exit the loop
        try:
            button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, "DataTables_Table_0_next")), message="Button not clickable within 2 seconds.")
            button.click()
            time.sleep(2)
            # Get the updated HTML content and parse it using BeautifulSoup
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
        except TimeoutException:
            print("Button not found or not clickable within 10 seconds.")
            break
        count += 1

# Close the browser
driver.quit()

# dans cette partie, je separer les differentes sanctions prononcees dans un meme dossier
with open('output1.csv', mode='r') as input_file, open('output2.csv', mode='w', newline='') as output_file:
    reader = csv.reader(input_file, delimiter=',', quotechar='"')
    writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for row in reader:
        # Split the "montant" column by comma and write each element as a separate column
        montant = re.split('\n(?=\d)', row[2])
        writer.writerow([row[0], row[1]] + montant)

# dans cette partie, je transforme les montants en chiffres

with open('output2.csv', mode='r') as input_file, open('sanctions_amf.csv', mode='w', newline='') as output_file:
    reader = csv.reader(input_file, delimiter=',', quotechar='"')
    writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for row in reader:
        row[2] = re.sub(r'\D', '', row[2])  # Remove all non-digit characters from column 2
        writer.writerow(row)

os.remove("output1.csv")
os.remove("output2.csv")