from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service=service, options=options)

url = "https://www.producthunt.com/search?q=mental+health+ai"

driver.get(url)

time.sleep(20)

page_source = driver.page_source

with open("source_producthunt.html", "w", encoding="utf-8") as fichier:
    fichier.write(page_source)

driver.quit()