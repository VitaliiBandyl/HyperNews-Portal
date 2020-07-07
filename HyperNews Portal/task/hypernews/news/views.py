from django.shortcuts import render
from django.views.generic.base import View

from .utils import get_article


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