from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework import status

from .models import Todo
from .serializers import UserSerializer


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
