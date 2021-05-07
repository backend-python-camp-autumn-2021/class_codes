from django.contrib.auth.models import User

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
