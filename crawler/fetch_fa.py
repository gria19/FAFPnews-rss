import requests
from bs4 import BeautifulSoup
import os  

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Cookie": os.getenv("FA_COOKIE")
}

FA_URL = "https://www.foreignaffairs.com/articles"

def fetch_latest_fa_articles():
    response = requests.get(FA_URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []
    for item in soup.select("article h2 a")[:5]:
        title = item.text.strip()
        url = item['href']
        if not url.startswith("http"):
            url = "https://www.foreignaffairs.com" + url
        articles.append({"title": title, "url": url})

    return articles
