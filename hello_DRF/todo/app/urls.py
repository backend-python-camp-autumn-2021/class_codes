from django.urls import path, include

from .views import TodoListView

urlpatterns = [
    path("", TodoListView.as_view(), name="list_todos"),
]
