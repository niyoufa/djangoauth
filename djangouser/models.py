#coding=utf-8

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class ProfileBase(type):  # 对于传统类，他们的元类都是types.ClassType
    def __new__(cls, name, bases, attrs):  # 带参数的构造器，__new__一般用于设置不变数据类型的子类
        module = attrs.pop('__module__')
        parents = [b for b in bases if isinstance(b, ProfileBase)]
        if parents:
            fields = []
            for obj_name, obj in attrs.items():
                if isinstance(obj, models.Field): fields.append(obj_name)
                User.add_to_class(obj_name, obj)
            UserAdmin.fieldsets = list(UserAdmin.fieldsets)
            UserAdmin.fieldsets.append((name, {'fields': fields}))
        return super(ProfileBase, cls).__new__(cls, name, bases, attrs)


class ProfileUser(object):
    __metaclass__ = ProfileBase  # 类属性


class MyProfile(ProfileUser):
    real_name = models.CharField(max_length=255)  # 真实姓名
    level = models.IntegerField(default=0)  # 级别