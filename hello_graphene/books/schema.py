import graphene
from graphene_django.types import DjangoObjectType, ObjectType

from .models import Author, Book


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        # fields = ("id", "name")


class BookType(DjangoObjectType):
    class Meta:
        model = Book


class Query(ObjectType):
    author = graphene.Field(AuthorType, id=graphene.Int())
    book = graphene.Field(BookType, id=graphene.Int())
    all_authors = graphene.List(AuthorType)
    all_books = graphene.List(BookType)
