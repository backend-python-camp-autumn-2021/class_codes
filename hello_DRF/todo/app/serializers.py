from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import serializers

from .models import Todo


class ListTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title', 'done', 'due_date']


class UserSerializer(serializers.ModelSerializer):
    todos = ListTodoSerializer(many=True)

    class Meta:
        model = User
        fields = ['username', 'todos']

    def update(self, instance, validated_data):
        for todo in validated_data["todos"]:
            Todo.objects.create(user=instance, **todo)
        return instance


class TodoListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'url', 'title', 'due_date']

    def create(self, validated_data):
        # user = get_object_or_404(User, username=self.context["username"])
        todo = Todo.objects.create(
            user=self.context["request"].user, **validated_data)
        return todo


class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
