from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer


class TodoListView(APIView):

    def get(self, request, format=None):
        todos_qs = Todo.objects.all()
        serilized_data = TodoSerializer(todos_qs, many=True)
        return Response(serilized_data.data)
