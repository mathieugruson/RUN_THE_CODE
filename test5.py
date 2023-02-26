from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Initialize the webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

# Define the starting page and current page number
start_url = 'https://www.amf-france.org/fr/sanction-transaction/Decisions-de-la-commission-des-sanctions'
current_page = 1

while True:
    # Navigate to the current page
    url = f'{start_url}?page={current_page}'
    driver.get(url)

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

    try:
        cookie_banner = driver.find_element_by_id('tarteaucitronAlertBig')
        cookie_banner.find_element_by_class_name('tarteaucitronClose').click()
    except NoSuchElementException:
        pass

    # Check if there is a link to the next page
    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="DataTables_Table_0_next"]')))
    if not next_button:
        break

    # Navigate to the next page
    current_page += 1
    next_button.click()