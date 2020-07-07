import json
from django.conf import settings


def get_article(slug: str):
    """Takes a article slug and returns correspond article"""
    with open(settings.NEWS_JSON_PATH, 'r') as f:
        news = json.load(f)
        for article in news:
            if article.get('link') == slug:
                return article
