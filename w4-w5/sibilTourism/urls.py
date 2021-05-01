from xml.etree.ElementInclude import include

from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

def index(request):
    return render(request, "index.html", {})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="home"),
    path('profile/',include("user.urls")),
    path('product_present/',include("product_present.urls")),
    path("accounts/" , include("django.contrib.auth.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
