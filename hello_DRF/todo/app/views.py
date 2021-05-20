from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView, ListAPIView
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.authentication import BaseAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination

from .models import Todo
from .serializers import UserSerializer, TodoListSerializer, TodoDetailSerializer
from .permissions import IsSuperUser


class UsersTodoListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ['username']


class UsersTodoListViewBaBadBakhti(APIView):
    # permission_classes = [IsSuperUser]
    # authentication_classes = [TokenAuthentication]

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
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TodoListSerializer

    def get_queryset(self):
        # queryset = super().get_queryset()
        # if not self.request.query_params.get("username", None):
        #     raise APIException(
        #         detail="username field needed in url params", code=400)
        # username = self.request.query_params.get("username")
        # queryset = Todo.objects.filter(user__username=username)
        queryset = Todo.objects.filter(user=self.request.user)
        print(queryset)
        return queryset

    # def get_serializer_context(self):
    #     """
    #     Extra context provided to the serializer class.
    #     """
    #     serializer_context = super().get_serializer_context()
    #     # serializer_context["username"] = self.request.query_params.get(
    #     #     "username")
    #     # serializer_context.update({"user": self.request.user})
    #     return serializer_context


class TodoDetail(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all()
    serializer_class = TodoDetailSerializer


class DeleteTodoView(DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all()
    serializer_class = TodoDetailSerializer
