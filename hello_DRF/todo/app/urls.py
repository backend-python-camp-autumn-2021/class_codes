from django.urls import path, include

from .views import (UsersTodoListViewBaBadBakhti,
                    UsersTodoListView, TodoList, TodoDetail, DeleteTodoView)

urlpatterns = [
    path("", UsersTodoListView.as_view(), name="all-user-todo-list"),
    path("todo/", TodoList.as_view(), name="todo-list"),
    path("todo-delete/<int:pk>", DeleteTodoView.as_view(), name="todo_delete"),
    path("todo/<int:pk>", TodoDetail.as_view(),
         name="todo-detail"),
]
