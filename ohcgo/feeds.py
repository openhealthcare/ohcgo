"""
Return the interesting bits from the blog.
"""
import feedparser

def recent_posts():
    """
    Get me the three most recent posts from the OHC blog.
    """
    d = feedparser.parse('http://www.openhealthcare.org.uk/?feed=rss2')
    entries = d['entries'][:3]
    return [dict(title=e['title'],
                  link=e['link'],
                  description=e['description'][:-5])
             for e in entries]
