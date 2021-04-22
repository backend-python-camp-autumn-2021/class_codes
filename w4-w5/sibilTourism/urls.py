from xml.etree.ElementInclude import include

from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


def index(request):
    return HttpResponse("Home page")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="home"),
    path('profile/',include("user.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
