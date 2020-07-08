from django.shortcuts import render
from django.views.generic.base import View

from .utils import get_article, get_all_news


class HomePage(View):
    """Home page"""

    def get(self, request):
        context = {'information': 'Coming soon'}
        return render(request, 'news/home.html', context=context)


class NewsDetailPage(View):
    """Page detail view"""

    def get(self, request, slug):
        context = get_article(slug)
        return render(request, 'news/article.html', context=context)


class NewsListPage(View):
    """Page list view"""

    def get(self, request):
        context = {'news': get_all_news()}
        return render(request, 'news/news_list.html', context=context)