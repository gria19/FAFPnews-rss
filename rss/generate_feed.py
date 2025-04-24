from feedgen.feed import FeedGenerator
from datetime import datetime

def generate_rss(feed_items, output_file="rss.xml"):
    fg = FeedGenerator()
    fg.id("https://foreignpolicy.com/")
    fg.title("Foreign News Digest")
    fg.link(href="https://foreignpolicy.com", rel="alternate")
    fg.description("Latest summarized news from Foreign Policy and Foreign Affairs")
    fg.language("zh")

    for item in feed_items:
        fe = fg.add_entry()
        fe.id(item["url"])
        fe.title(item["title"])
        fe.link(href=item["url"])
        fe.description(item["summary"])
        fe.pubDate(datetime.now(timezone.utc))  # ✅ 有时区信息

    fg.rss_file(output_file, pretty=True)
