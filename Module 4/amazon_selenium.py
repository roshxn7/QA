from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open Amazon's homepage
driver.get("https://www.amazon.in")

# Wait for the page to load
time.sleep(2)

# Search for a specific product
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("laptop")
search_box.send_keys(Keys.RETURN)

# Wait for the search results to load
time.sleep(2)

# Extract information about the first 5 search results
results = driver.find_elements(By.CSS_SELECTOR, ".s-main-slot .s-result-item")[2:7]
for result in results:
    try:
        title = result.find_element(By.CSS_SELECTOR, "h2 a span").text
    except:
        title = "N/A"

    try:
        price = result.find_element(By.CSS_SELECTOR, ".a-price-whole").text
    except:
        price = "N/A"

    try:
        rating = result.find_element(By.CSS_SELECTOR, ".a-icon-alt").get_attribute("innerHTML")
    except:
        rating = "N/A"

    try:
        reviews = result.find_element(By.CSS_SELECTOR, ".s-link-style .a-size-base").text
    except:
        reviews = "N/A"

    print(f"Product Title: {title}")
    print(f"Price: ${price}")
    print(f"Rating: {rating}")
    print(f"Number of Reviews: {reviews}")
    print("-" * 20)

# Close the browser
driver.quit()