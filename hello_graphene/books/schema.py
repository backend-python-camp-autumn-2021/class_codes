import graphene

from django.shortcuts import get_object_or_404

from graphene_django.types import DjangoObjectType, ObjectType

from .models import Author, Book


# class AuthorType(ObjectType):
#     id = graphene.ID()
#     name = graphene.String()
#     birth_year = graphene.Int()

class AuthorType(DjangoObjectType):

    class Meta:
        model = Author
        # exclude = ("id",)


class BookType(DjangoObjectType):
    class Meta:
        model = Book


class Query(ObjectType):
    author = graphene.Field(AuthorType, id=graphene.Int())
    book = graphene.Field(BookType, id=graphene.Int())
    all_authors = graphene.List(AuthorType, name="_all_authors")
    all_books = graphene.List(BookType)
    ok = graphene.Boolean()

    def resolve_author(root, info, id):
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

    def resolve_ok(self, info):
        print(info.context.user)
        return True


class AuthorInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    birth_year = graphene.Int()


class CreateAuthor(graphene.Mutation):
    class Arguments:
        input = AuthorInput(required=True)

    created = graphene.Boolean()
    author = graphene.Field(AuthorType)
    error_msg = graphene.String()

    @staticmethod
    def mutate(self, info, input=None):
        try:
            author_obj = Author.objects.create(
                name=input.name, birth_year=input.birth_year)
            created = True
            return CreateAuthor(created=created, author=author_obj, error_msg=None)
        except Exception as e:
            created = False
            return CreateAuthor(created=created, author=None, error_msg=e)


class UpdateAuthor(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = AuthorInput(required=True)

    created = graphene.Boolean()
    author = graphene.Field(AuthorType)

    @staticmethod
    def mutate(self, info, id, input=None):
        created = False
        author_obj = get_object_or_404(Author, pk=id)
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
