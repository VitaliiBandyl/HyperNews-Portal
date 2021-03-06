from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view()),
    path('news/', views.NewsListPage.as_view()),
    path('news/create/', views.NewsCreatePage.as_view()),
    path('news/<int:slug>/', views.NewsDetailPage.as_view()),
]