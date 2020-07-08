from django.shortcuts import render, redirect
from django.views.generic.base import View

from .utils import get_article, get_all_news, create_news


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


class NewsCreatePage(View):
    """Create News view"""

    def get(self, request):
        return render(request, 'news/create_news.html')

    def post(self, request):
        title = request.POST.get('title')
        text = request.POST.get('text')
        create_news(title, text)
        return redirect('/news/')