from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

options = webdriver.ChromeOptions()

options.add_argument(r"--user-data-dir=C:\Users\rhahl\OneDrive\Bureau\selenium_profile")
options.add_argument("--profile-directory=Default")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

driver.get("https://www.producthunt.com/search?q=mental+health+ai")

input("Finish the security check manually, then press Enter...")

products = driver.find_elements(
    By.CSS_SELECTOR,
    "button[data-test^='spotlight-result-product-']"
)

data = []

for product in products:
    try:
        title = product.find_element(By.CSS_SELECTOR, "span.text-base").text
        desc = product.find_element(By.CSS_SELECTOR, "span.text-sm").text

        data.append({
            "Title": title,
            "Description": desc
        })
    except:
        pass

driver.quit()

df = pd.DataFrame(data)
df.to_csv("products.csv", index=False, encoding="utf-8")

print(df)