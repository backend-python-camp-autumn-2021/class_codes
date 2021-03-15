from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from .models import Article, Category


@csrf_exempt
def show_articles(request):
    # print(dir(request))
    # print("request.POST: ", request.POST)
    # print("request.GET: ", query_url)
    # print("cookiie", request.COOKIES)
    # print(request.method)
    # print(cat)

    query_url = request.GET
    cat = query_url.get('cat', None)

    if cat:
        cat = get_object_or_404(Category, name=cat)
        articles = cat.article_set.all()

    else:
        articles = Article.objects.all()  # QuerySet

    result = []
    for elm in articles:  # query ashghal
        result.append(
            {
                "title": elm.title,
                "author": elm.author.nick_name,
                "context": elm.context,
                "published": elm.date_pub,
                "slug": elm.slug
            }
        )

    return JsonResponse(result, safe=False)


def article(request, slug=None):
    if request.method == 'GET':
        article = get_object_or_404(Article, slug=slug)
        result = {
            "title": article.title,
            "author": article.author.nick_name,
            "context": article.context,
            "published": article.date_pub,
        }
        return JsonResponse(result)


def article_create(request):
    pass
