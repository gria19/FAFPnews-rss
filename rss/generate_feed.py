from feedgen.feed import FeedGenerator
from datetime import datetime


def generate_rss(feed_items, output_file="rss.xml"):
    fg = FeedGenerator()
    fg.title("Foreign News Digest")
    fg.link(href="https://www.foreignaffairs.com", rel="alternate")
    fg.description("Latest summarized news from Foreign Policy and Foreign Affairs")

    for item in feed_items:
        fe = fg.add_entry()
        fe.title(item["title"])
        fe.link(href=item["url"])
        fe.description(item["summary"])
        fe.pubDate(datetime.utcnow())

    fg.rss_file(output_file)
