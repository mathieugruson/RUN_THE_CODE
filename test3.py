from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import time
import csv
import re

# # Create a new instance of the Chrome driver
# # The line of code driver = webdriver.Chrome() is used to create an instance of the Chrome web driver in Python using the Selenium library.
# #Selenium is a popular library used for automating web browsers, and it provides a way to control web browsers through Python code. The webdriver module in Selenium provides a way to interact with various web browsers, including Google Chrome, Firefox, Safari, and others.
# #The webdriver.Chrome() function creates a new instance of the Chrome web driver, which allows you to control the Chrome browser through your Python code. Once you have created a driver instance, you can use various methods provided by Selenium to interact with the browser, such as navigating to a URL, clicking on links and buttons, filling out forms, and more.
# driver = webdriver.Chrome()

# # Navigate to the web page
# url = 'https://www.amf-france.org/fr/sanction-transaction/Decisions-de-la-commission-des-sanctions'
# driver.get(url)

# # Wait for the dynamic content to load
# time.sleep(10)

# # Get the HTML content of the page after dynamic content has loaded
# html = driver.page_source

# # Parse the HTML content using BeautifulSoup
# soup = BeautifulSoup(html, 'html.parser')

# # Click the "refuser tout" button to disable cookie consent
# button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tarteaucitronAllDenied2")))
# button.click()

# # Write to CSV
# with open('output1.csv', mode='w') as output_file:
#     output_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     output_writer.writerow(['date', 'theme', 'montant'])

#     # Keep scraping the page until the "next page" button is disabled
#     count = 0
#     while count < 41:
#         # Get all <p> tags in the page that contain the Euro symbol
#         p_tags = [p for p in soup.find_all('p') if '€' in p.get_text() or 'euros' in p.get_text()]

#         # Get all <span> tags with class="tag"
#         s_tags = [s for s in soup.find_all('span', {'class': 'tag'})]

#         # Get all <span> tags with class="date"
#         d_tags = [d for d in soup.find_all('span', {'class': 'date'})]

#         # Write the data to the CSV file
#         for p, s, d in zip(p_tags, s_tags, d_tags):
#             year = d.get_text().split()[-1]  # Extract the last word of the date string
#             output_writer.writerow([year, s.get_text(), p.get_text()])
#         # Click the "next page" button if it's clickable, otherwise exit the loop
#         try:
#             button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, "DataTables_Table_0_next")), message="Button not clickable within 2 seconds.")
#             button.click()
#             time.sleep(2)
#             # Get the updated HTML content and parse it using BeautifulSoup
#             html = driver.page_source
#             soup = BeautifulSoup(html, 'html.parser')
#             print("Clicked the next page button.")
#         except TimeoutException:
#             print("Button not found or not clickable within 10 seconds.")
#             break
#         count += 1

# print("test")

# # Close the browser
# driver.quit()

import csv

with open('output1.csv', mode='r') as input_file, open('output_file2.csv', mode='w', newline='') as output_file:
    reader = csv.reader(input_file, delimiter=',', quotechar='"')
    writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for row in reader:
        # Split the "montant" column by comma and write each element as a separate column
        montant = re.split('\n(?=\d)', row[2])
        writer.writerow([row[0], row[1]] + montant)

