#coding=utf-8

from rest_framework import serializers
from djangouser.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'groups')