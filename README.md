# AMF Sanctions Scraper

This project is a web scraper for extracting sanction decisions from the [AMF France Sanctions Page](https://www.amf-france.org/fr/sanction-transaction/Decisions-de-la-commission-des-sanctions). It uses Python, Selenium, and BeautifulSoup to scrape data from the dynamic web page, extract specific information, and output it to CSV files.

The script collects:

- Date of the sanction decision
- Theme of the sanction
- Amount of the fine (in euros)

After scraping, it cleans the data by splitting sanctions that are grouped together in one row, then formats the amounts by removing non-digit characters, outputting clean data to a final CSV file.

## Why I Created This

I started working on this project to help a friend in EFB school at a time when I had very little knowledge of programming. I brute-forced my way through this using **ChatGPT**. The AI helped me step-by-step as I learned how to scrape, process, and clean data from a website. This experience taught me a lot about web scraping and Python automation.

It's not the most elegant code, but it works! And it's a testament to learning by doing—even when you don’t fully know what you’re doing.

## Requirements

- Python 3.x
- Chrome WebDriver
- Required Python packages: `selenium`, `beautifulsoup4`