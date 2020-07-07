from django.shortcuts import render
from django.views.generic.base import View


class HomePage(View):
    """Home page"""

    def get(self, request):
        context = {'information': 'Coming soon'}
        return render(request, 'news/home.html', context=context)
