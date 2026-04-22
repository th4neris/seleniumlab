import requests
from bs4 import BeautifulSoup
import pandas as pd
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7,ar-MA;q=0.6,ar;q=0.5,ru-RU;q=0.4,ru;q=0.3,es-US;q=0.2,es;q=0.1",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}
data = []

for page in range(1, 11): 
    url = f"https://github.com/search?q=mental+health+ai&type=repositories&p={page}"

    response = requests.get(url, headers=headers)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    repos = soup.find_all("div", class_="Repositories-module__resultContent___BS2W")
    for repo in repos:
           repo_name = repo.find("a",href = True).get("href")
           date = repo.find("ul").find("div", class_="prc-Truncate-Truncate-2G1eo").find("span").text

           title_try = repo.find("span", class_="search-match SearchMatchText-module__searchMatchText__n6aQc prc-Text-Text-9mHv3")
           if title_try:
                 title = title_try.text.strip()
                 
                 

           data.append({
                "Repository name": repo_name, 
                "Updated": date,
                "Title": title
           })

df = pd.DataFrame(data)
df.to_csv("repos.csv", index=False)

    

           

    