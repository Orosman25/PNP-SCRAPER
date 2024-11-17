from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--disable-gpu")  
chrome_options.add_argument("--no-sandbox")  


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


with open('cart.txt', 'r') as file:
    urls = file.readlines()


with open('price.txt', 'w') as price_file:
    for url in urls:
        url = url.strip() 
        
   
        print(f"Debugging: Opening URL: {url}")
        driver.get(url)
        
       
        print("Debugging: Waiting for the page to load...")
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
 
        print("Debugging: Attempting to find product name element...")
        try:
            product_name_element = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'h2'))
            )
            product_name = product_name_element.text
            print(f"Debugging: Found product name: {product_name}")
        except Exception as e:
            print(f"Error: Failed to find product name. {e}")
            product_name = "N/A"
        

        print("Debugging: Attempting to find product price element...")
        try:
            product_price_element = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/pnp-root/div/ui-storefront/main/cx-page-layout/cx-page-slot[4]/cms-product-summary/div/cms-price/div/div/div/div"))
            )
            product_price = product_price_element.text
            print(f"Debugging: Found product price: {product_price}")
        except Exception as e:
            print(f"Error: Failed to find product price. {e}")
            product_price = "N/A"

        price_file.write(f"{product_name}: {product_price}\n")
        

        print(f"Debugging: Product Name: {product_name}")
        print(f"Debugging: Product Price: {product_price}")


driver.quit()
