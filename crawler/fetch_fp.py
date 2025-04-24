import requests
from bs4 import BeautifulSoup
import os

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/112.0.0.0 Safari/537.36",
    "Cookie": os.getenv("FP_COOKIE")
}

FP_URL = "https://foreignpolicy.com/latest/"

def fetch_latest_fp_articles():
    response = requests.get(FP_URL, headers=HEADERS)
    
    # ✅ 调试打印：网页返回的内容（前2000字）
    print("📄 Foreign Policy 页面返回 HTML：")
    print(response.text[:2000])  # 调试用，查看页面结构或是否为登录页

    soup = BeautifulSoup(response.text, 'html.parser'
