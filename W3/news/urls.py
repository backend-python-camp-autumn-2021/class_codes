from django.urls import path

from .views import show_articles, article, article_create


urlpatterns = [
    path('', show_articles),
    path('article/<str:slug>', article),
    path('article_create/', article_create)
]
