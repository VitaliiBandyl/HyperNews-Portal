import json
from django.conf import settings


def get_article(slug: str):
    """Takes a article slug and returns correspond article"""
    with open(settings.NEWS_JSON_PATH, 'r') as f:
        news = json.load(f)
        for article in news:
            if article.get('link') == slug:
                return article


def get_all_news():
    """Return all News"""
    with open(settings.NEWS_JSON_PATH, 'r') as f:
        news: list = json.load(f)
        news.sort(key=lambda x: x['created'], reverse=True)

        context = {}
        for article in news:
            date = article['created'].split()[0]
            context.setdefault(date, []).append(article)

        return context
