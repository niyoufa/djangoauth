#coding=utf-8
from django.db import models
from django.contrib.auth.models import User as BaseUser
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group

class User(BaseUser):
    role = models.IntegerField()