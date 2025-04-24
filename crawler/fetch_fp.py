import feedparser

def fetch_latest_fp_articles():
    feed = feedparser.parse("https://foreignpolicy.com/feed/")
    articles = []
    
    for entry in feed.entries[:5]:
        articles.append({
            "title": entry.title,
            "url": entry.link,
            "content": entry.description  # ✅ 直接当正文传给 GPT
        })

    return articles
