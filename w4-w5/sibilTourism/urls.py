from xml.etree.ElementInclude import include

from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include


def index(request):
    return HttpResponse("Home page")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="home"),
    path('profile/',include("user.urls")),
]
