from django.shortcuts import render, redirect
from django.views.generic.base import View

from .utils import get_article, get_news, create_news


class HomePage(View):
    """Home page"""

    def get(self, request):
        return redirect('/news/')


class NewsDetailPage(View):
    """Page detail view"""

    def get(self, request, slug):
        context = get_article(slug)
        return render(request, 'news/article.html', context=context)


class NewsListPage(View):
    """Page list view"""

    def get(self, request):

        if request.GET:
            # If search parameters are passed, it searches for them
            news = get_news(request.GET.get('q'))
        else:
            # If search parameters are not passed returns all news
            news = get_news()
        context = {'news': news}
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