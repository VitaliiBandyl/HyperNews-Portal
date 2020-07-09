import json
from datetime import datetime

from django.conf import settings


def get_article(slug: str):
    """Takes a article slug and returns correspond article"""
    with open(settings.NEWS_JSON_PATH, 'r') as f:
        news = json.load(f)
        for article in news:
            if article.get('link') == slug:
                return article


def get_news(search=None):
    """If search parameters are passed, it searches for them,
    otherwise returns all results"""
    with open(settings.NEWS_JSON_PATH, 'r') as f:
        news: list = json.load(f)
        news.sort(key=lambda x: x['created'], reverse=True)
        context = {}
        for article in news:
            date = article['created'].split()[0]
            if search:
                if search.lower() in article['title'].lower():
                    context.setdefault(date, []).append(article)
            else:
                context.setdefault(date, []).append(article)

        return context


def create_news(title, text):
    """Created new article and storage is JSON file"""

    with open(settings.NEWS_JSON_PATH, 'r') as news_json_file:
        news_feed = json.load(news_json_file)
    with open(settings.NEWS_JSON_PATH, 'w') as news_json_file:
        news_item = {
            'created': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'text': text,
            'title': title,
            'link': int(datetime.timestamp(datetime.now()) * 1000),
        }
        news_feed.append(news_item)
        json.dump(news_feed, news_json_file)
