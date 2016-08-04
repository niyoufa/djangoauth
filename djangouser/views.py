#coding=utf-8

import pdb

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from djangouser.models import User
from djangouser.serializers import UserSerializer


class Login(APIView):
    """
    user login
    """
    def post(self,request,format=None):
        try:
            params = request.data
            username = params['username']
            password = params["password"]
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    csrf_token = request.META["CSRF_COOKIE"]
                    serializer = UserSerializer(user)
                    data = serializer.data
                    data.update({
                        "csrf_token":csrf_token,
                    })
                    return Response(data, status=status.HTTP_201_CREATED)
                else:
                    return Response({"error":"The password is valid, but the account has been disabled!"},
                                    status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error":"The username and password were incorrect."},
                                status=status.HTTP_400_BAD_REQUEST)

        except Exception,e:
            return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(user, status=status.HTTP_201_CREATED)

class Logout(APIView):
    """
    user logout
    """
    def post(self,request):
        try:
            logout(request)
        except Exception,e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({}, status=status.HTTP_201_CREATED)



