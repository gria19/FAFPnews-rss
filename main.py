from crawler.fetch_fp import fetch_latest_fp_articles
from crawler.fetch_fa import fetch_latest_fa_articles
from summarizer.summarize import summarize_article
from rss.generate_feed import generate_rss
import requests
from bs4 import BeautifulSoup


def get_article_content(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        return '\n'.join(p.get_text() for p in paragraphs[:10])  # 只取前 10 段文字
    except:
        return ""


def main():
    articles = fetch_latest_fp_articles() + fetch_latest_fa_articles()
    feed_items = []

    for article in articles:
        content = get_article_content(article["url"])
        if not content:
            continue
        summary = summarize_article(article["title"], content)
        feed_items.append({
            "title": article["title"],
            "url": article["url"],
            "summary": summary
        })

    generate_rss(feed_items)


if __name__ == "__main__":
    main()

print("🔍 获取文章链接中...")
articles = fetch_latest_fp_articles() + fetch_latest_fa_articles()
print(f"✅ 抓到 {len(articles)} 篇文章")

feed_items = []

for article in articles:
    print(f"🌐 正在抓取正文：{article['title']} - {article['url']}")
    content = get_article_content(article["url"])
    if not content:
        print("⚠️ 正文抓取失败，跳过")
        continue
    print("✏️ 调用 ChatGPT 生成摘要")
    summary = summarize_article(article["title"], content)
    feed_items.append({
        "title": article["title"],
        "url": article["url"],
        "summary": summary
    })
