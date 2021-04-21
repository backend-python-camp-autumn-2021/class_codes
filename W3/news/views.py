import json
import logging
import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from .models import Article, Category, User, Author

logger = logging.getLogger(__name__)


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


def article_list(request):
    logger.warning(
        f"karbar ba {request.META.get('REMOTE_ADDR')} be system vasl shod")
    if request.method == 'GET':
        # query_set = Article.objects.all()
        # query_set = Article.objects.filter(
        #     title__startswith='hello') | Article.objects.filter(title__startswith='bye')

        query_set = Article.objects.prefetch_related('category').filter(
            date_pub__day__gt=datetime.datetime.today().day - 20).filter(title__startswith="hello")

        result = []
        for article in query_set:
            article_cats = []
            for cat_item in article.category.all():
                article_cats.append(cat_item.name)
            result.append({
                "title": article.title,
                "author": article.author.nick_name,
                "context": article.context,
                "published": article.date_pub,
                "path": article.get_absolute_url(),
                "cats": article_cats
            })
        return JsonResponse(result, safe=False)


def article_detail(request, slug=None):
    if request.method == 'GET':
        article = get_object_or_404(Article, slug=slug)
        result = {
            "title": article.title,
            "author": article.author.nick_name,
            "context": article.context,
            "published": article.date_pub,
        }

        print(request.session)
        request.session['name'] = 'ashkan'

        if not request.session.get('seen', None):
            request.session['seen'] = []
            request.session['seen'].append(article.slug)
            article.seen_num += 1
            article.save()
        elif article.slug not in request.session['seen']:
            request.session['seen'].append(article.slug)
            article.seen_num += 1
            article.save()

        # TODO
        # print(str(article.slug))
        # if not request.COOKIES.get('seen', None):
        #     response = JsonResponse(result)
        #     response.set_cookie('seen', [str(article.slug)])
        #     article.seen_num += 1
        #     article.save()
        #     return response
        # elif article.slug not in request.COOKIES['seen']:
        #     response = JsonResponse(result)
        #     new_seen = request.COOKIES['seen']
        #     new_seen.append([str(article.slug)])
        #     response.set_cookie('seen', new_seen)
        #     article.seen_num += 1
        #     article.save()

        return JsonResponse(result)


@ csrf_exempt
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


def article_update(request):
    pass


def article_delete(request):
    pass


class A:
    def __init__(self, age):
        self.age = age

    def ghol_mehrdad(self):
        return "nadidan bad panjah be sharte nabudan shaghayegh"


def index(request):
    print(request.POST)
    a = A(60)
    context = {'age': a}
    return render(request, 'index.html', context)


def home(request):
    query_set = Article.objects.select_related('author').all()
    result = []
    for article in query_set:
        result.append({
            "title": article.title,
            # "author": article.author.nick_name,
            "context": article.context,
            "published": article.date_pub,
            "path": article.get_absolute_url(),
        })
    return render(request, 'home.html', {'articles': result})
