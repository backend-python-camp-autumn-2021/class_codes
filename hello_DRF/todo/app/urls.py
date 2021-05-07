from django.urls import path, include

from .views import UsersTodoListViewBaBadBakhti

urlpatterns = [
    path("", UsersTodoListViewBaBadBakhti.as_view(), name="todo-list"),
]
