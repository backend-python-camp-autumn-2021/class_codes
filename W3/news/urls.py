from django.urls import path

from .views import show_articles, article


urlpatterns = [
    path('', show_articles),
    path('article/<str:slug>', article),
]
