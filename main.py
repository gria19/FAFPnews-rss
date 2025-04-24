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
