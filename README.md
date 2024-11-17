This document provides instructions for setting up and running the PNP Scraper, a Python script designed to extract product names and prices from Pick n Pay product pages.

# Features
- Automated Scraping: Utilizes Selenium for automated web interaction and data extraction.
- Headless Mode: Runs without opening a browser window, ideal for background tasks.
- Product Data Extraction: Scrapes product names and prices.
- Customizable: Can be modified to extract additional data like images and descriptions.

# Requirements
- Python 3.6 or higher (download from https://www.python.org/downloads/)
- Required Libraries (listed in requirements.txt)

# Installation
## 1. Install Python:
Follow the official Python installation guide: https://www.python.org/downloads/

Setup Instructions
Step 1: Clone the Repository
Clone the repository to your local machine:

```bash
git clone https://github.com/Orosman25/pnp-scraper.git
cd pnp-scraper
pip install -r requirements.txt
```
Step 2: Run the Scraper
Once you have the repository cloned and dependencies installed, you can run the scraper script with the following command:
```bash
python PNP-SCRAPER.py
```
Script Functionality
Open each URL for scraping.
Wait for the page to load fully.
Extract the product name and price.
Save the extracted data to a file named price.txt.
Step 3: Check the Output
After the script finishes running, you will find a price.txt file in the same directory. The file will contain the product names and their corresponding prices in the following format:

Example price.txt:
```bash
Product 1: R199.99
Product 2: R299.99
```

