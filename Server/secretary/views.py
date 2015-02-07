from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.contrib.auth.models import AnonymousUser

class Hello(APIView):
    permission_classes = (permissions.AllowAny, )
    def get(self, request, format=None):
        if isinstance(request.user, AnonymousUser):
            return Response(0)
        else:
            return Response({'username': request.user.username})

class Home(APIView):
    permission_classes = (permissions.AllowAny, )
    def get(self, request, format=None):
        return Response('welcome, but you can not do anything with non-api!')