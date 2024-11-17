# PNP Scraper

PNP Scraper is a Python-based web scraper designed to extract product names and prices from product pages on the PNP (Pick n Pay) website. This scraper uses Selenium to automate the web interaction and can run in headless mode (without opening a browser window). It is ideal for scraping product details from a list of URLs stored in a text file.

## Features

- **Automated Scraping**: Uses Selenium to visit product pages and extract data automatically.
- **Headless Mode**: Runs without a visible browser window, making it efficient for background operations.
- **Product Data Extraction**: Scrapes product names and prices.
- **Customizable**: You can modify the script to extract additional information, such as product images, descriptions, etc.

## Requirements

Before running the script, you need to install some Python libraries. These are listed in the `requirements.txt` file. Follow these steps to install them:

### Step 1: Install Python

Make sure you have Python 3.6 or higher installed. You can download Python from [here](https://www.python.org/downloads/).

### Step 2: Install Required Libraries

Create a virtual environment (optional but recommended) and install the necessary libraries using `pip`:

```bash
pip install -r requirements.txt
