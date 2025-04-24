import requests
from bs4 import BeautifulSoup
import os  

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/112.0.0.0 Safari/537.36",
    "Cookie": os.getenv("FP_COOKIE")  # 从 GitHub Secrets 获取 cookie
}

FP_URL = "https://foreignpolicy.com/latest/"

def fetch_latest_fp_articles():
    response = requests.get(FP_URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []
    for item in soup.select("article a.card-title")[:5]:  # 抓最新5篇
        title = item.text.strip()
        url = item["href"]
        if not url.startswith("http"):
            url = "https://foreignpolicy.com" + url
        articles.append({"title": title, "url": url})

    return articles

print(response.text[:2000])  # 打印前2000个字符
