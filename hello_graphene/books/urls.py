from django.urls import path, include

from graphene_django.views import GraphQLView

from .schema import schema

urlpatterns = [
    path('', GraphQLView.as_view(graphiql=True, schema=schema)),
]
