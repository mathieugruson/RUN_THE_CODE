import requests
from bs4 import BeautifulSoup
import time

# Make a request to the website
url = "https://www.amf-france.org/fr/sanction-transaction/Decisions-de-la-commission-des-sanctions"
response = requests.get(url)
# Check if the response was successful
time.sleep(10)

if response.status_code == 200:
    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, "html.parser")
    # Find all elements with class "dtr-data" and print their content
    data_elements = soup.find_all(class_="dtr-data")
    for element in data_elements:
        print(element.get_text().strip())
else:
    print("Request failed with status code:", response.status_code)