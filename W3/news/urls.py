from django.urls import path

from .views import home, index, show_articles, article_list, article_detail, article_create


urlpatterns = [
    path('a/', index),
    path('article/', article_list, name='article_list'),
    path('article/<str:slug>', article_detail, name='article_detail'),
    path('article_create/', article_create),
    path('', home, name='home'),
]
