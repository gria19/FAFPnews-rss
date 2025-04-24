import requests
from bs4 import BeautifulSoup
import os

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Cookie": os.getenv("FP_COOKIE")
}

FP_URL = "https://foreignpolicy.com/category/latest/"

def fetch_latest_fp_articles():
    response = requests.get(FP_URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')

    print("📄 Foreign Policy 页面返回 HTML（前2000字）：")
    print(response.text[:2000])  # 可删，用于调试

    articles = []

    for item in soup.select("div.card-component a.card-component__link")[:5]:
        title = item.get("aria-label") or item.text.strip()
        url = item["href"]
        if not url.startswith("http"):
            url = "https://foreignpolicy.com" + url
        articles.append({"title": title, "url": url})

    return articles
