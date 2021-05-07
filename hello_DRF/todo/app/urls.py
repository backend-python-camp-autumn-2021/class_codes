from django.urls import path, include

from .views import UsersTodoListViewBaBadBakhti, TodoList, TodoDetail

urlpatterns = [
    path("", UsersTodoListViewBaBadBakhti.as_view(), name="all-user-todo-list"),
    path("todo/", TodoList.as_view(), name="todo-list"),
    path("todo/<int:pk>", TodoDetail.as_view(),
         name="todo-detail"),
]
