from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.exceptions import APIException

from .models import Todo
from .serializers import UserSerializer, TodoListSerializer, TodoDetailSerializer


# class UsersTodoListView(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class UsersTodoListViewBaBadBakhti(APIView):

    def get(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not request.data.get("username", None):
            return Response({"username": "shalgham ino bezar"}, status=status.HTTP_400_BAD_REQUEST)
        user = get_object_or_404(User, username=request.data.get("username"))
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoList(ListCreateAPIView):
    serializer_class = TodoListSerializer

    def get_queryset(self):
        # queryset = super().get_queryset()
        if not self.request.query_params.get("username", None):
            raise APIException(
                detail="username field needed in url params", code=400)
        username = self.request.query_params.get("username")
        queryset = Todo.objects.filter(user__username=username)
        print(queryset)
        return queryset

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        serializer_context = super().get_serializer_context()
        serializer_context["username"] = self.request.query_params.get(
            "username")
        return serializer_context


class TodoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoDetailSerializer
