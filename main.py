from crawler.fetch_fp import fetch_latest_fp_articles
from crawler.fetch_fa import fetch_latest_fa_articles  # 如果你也抓 FA
from summarizer.summarize import summarize_article
from rss.generate_feed import generate_rss

import os
print("🔐 OPENAI_API_KEY =", os.getenv("OPENAI_API_KEY"))

print("🔍 获取文章链接中...")

# ✅ 如果你只抓 FP，则注释掉 FA 部分
articles = fetch_latest_fp_articles()
# articles = fetch_latest_fp_articles() + fetch_latest_fa_articles()

print(f"✅ 抓到 {len(articles)} 篇文章")

feed_items = []

for article in articles:
    print(f"🌐 正在生成摘要：{article['title']} - {article['url']}")
    content = article.get("content")
    if not content:
        print("⚠️ 无内容，跳过")
        continue

    summary = summarize_article(article["title"], content)
    feed_items.append({
        "title": article["title"],
        "url": article["url"],
        "summary": summary
    })

generate_rss(feed_items, "rss.xml")
