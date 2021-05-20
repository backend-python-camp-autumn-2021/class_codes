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


class AuthorInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    birth_year = graphene.Int()


class CreateAuthor(graphene.Mutation):
    class Arguments:
        input = AuthorInput(required=True)

    created = graphene.Boolean()
    author = graphene.Field(AuthorType)

    @staticmethod
    def mutate(root, info, input=None):
        created = True
        author_obj = Author(name=input.name, birth_year=input.birth_year)
        author_obj.save()
        return CreateAuthor(created=created, author=author_obj)


class UpdateAuthor(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = AuthorInput(required=True)

    created = graphene.Boolean()
    actor = graphene.Field(AuthorType)

    @staticmethod
    def mutate(root, info, id, input=None):
        created = False
        author_obj = Author.objects.get(pk=id)
        if author_obj:
            created = True
            author_obj.name = input.name
            author_obj.save()
            return UpdateAuthor(created=created, author=author_obj)
        return UpdateAuthor(created=created, author=None)


class Mutation(graphene.ObjectType):
    create_author = CreateAuthor.Field()
    update_author = UpdateAuthor.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
