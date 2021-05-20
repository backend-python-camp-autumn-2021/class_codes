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

    def resolve_author(self, info, id):
        try:
            return Author.objects.get(id=id)
        except Author.DoseNotExists:
            return None

    def resolve_book(self, info, id):
        try:
            return Book.objects.get(id=id)
        except Book.DoesNotExist:
            return None

    def resolve_all_authors(self, info):
        return Author.objects.all()

    def resolve_all_books(self, info):
        return Book.objects.all()


schema = graphene.Schema(query=Query)
