This document provides instructions for setting up and running the PNP Scraper, a Python script designed to extract product names and prices from Pick n Pay product pages.

Features
Automated Scraping: Utilizes Selenium for automated web interaction and data extraction.
Headless Mode: Runs without opening a browser window, ideal for background tasks.
Product Data Extraction: Scrapes product names and prices.
Customizable: Can be modified to extract additional data like images and descriptions.
Requirements
Python 3.6 or higher (download from https://www.python.org/downloads/)
Required Libraries (listed in requirements.txt)
Installation
1. Install Python:

Follow the official Python installation guide: https://www.python.org/downloads/

2. Install Required Libraries:

(Optional) Create a virtual environment to isolate project dependencies. Then, install libraries using pip:

Bash
pip install -r requirements.txt
Use code with caution.

Setup Instructions
1. Clone the Repository:

Use Git to clone the PNP Scraper repository to your local machine:

Bash
git clone https://github.com/your-username/pnp-scraper.git
cd pnp-scraper
Use code with caution.

2. Create cart.txt File:

In the project root directory, create a text file named cart.txt. Each line in this file should contain the URL of a product page you want to scrape.

Example cart.txt:

https://www.picknpay.co.za/some-product-1
https://www.picknpay.co.za/some-product-2
3. Run the Scraper:

Once cloned and dependencies installed, run the script with this command:

Bash
python scraper.py
Use code with caution.

Script Functionality
Opens each URL in the cart.txt file.
Waits for the page to load completely.
Extracts product name and price.
Saves extracted data to price.txt.
5. Check the Output:

After running the script, you'll find a price.txt file. It contains product names and corresponding prices:

Example price.txt:

Product 1: R199.99
Product 2: R299.99
6. Troubleshooting:

Missing data: If the script can't find the product name or price, it will print an error and use "N/A" as a placeholder. Check the product page structure or adjust the script to match specific elements.
Headless Mode: The script runs in headless mode by default (no browser window). To see the browser, comment out or remove the --headless option in the script.
Customization (Optional)
1. Scrape Additional Data:

Modify the script to extract additional information like descriptions or images. Use driver.find_element or driver.find_elements methods to target the appropriate HTML elements.

2. Change Output Format:

You can modify the script to save data in different formats (CSV, JSON) based on your needs.

Notes
Headless Mode: The script uses Chrome in headless mode. To see the browser, disable headless mode as mentioned earlier.
Dependencies: Ensure you have the correct library versions. Upgrade them using pip install --upgrade -r requirements.txt.
Web Scraping Ethics: Respect robots.txt guidelines to avoid violating terms of service. Use the script responsibly and avoid overwhelming the website.
Error Handling: Currently, the script handles errors by printing a message and continuing. You can modify it for more robust error handling.
