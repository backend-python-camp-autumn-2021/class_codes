from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    token = serializers.CharField(read_only=True)
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'token')

    def create(self, validated_data):
        user = super().create(validated_data)
        token = Token.objects.create(user=user)
        self.token = token.key
        return user

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['token'] = self.token
        return rep
