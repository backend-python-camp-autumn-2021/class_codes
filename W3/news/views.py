import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from .models import Article, Category, User, Author


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


@csrf_exempt
def article_create(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username", None)
        password = data.get("password", None)
        if username and password:
            user_obj = get_object_or_404(User, username=username)
            if user_obj.password == password:
                if Author.objects.filter(user=user_obj).exists():
                    author = Author.objects.get(user=user_obj)
                    category = data.pop("category")
                    region = data.pop("region")
                    data.pop("username")
                    data.pop("password")
                    # TODO cat multiple, exception handling(just get, if not exist error)
                    cat_obj = Category.objects.get(
                        name=category, region=region)
                    article = Article.objects.create(**data, author=author)
                    article.category.add(cat_obj)
                    article.save()
                else:
                    return JsonResponse({"status": "shoma mojaz be maghale neveshtan nistid"})
            else:
                return JsonResponse({"status": "shalgham passeto dorost bezan"})

        else:
            return JsonResponse({"status": "username and pass needed!"})

    return JsonResponse({"status": "just post method"})
