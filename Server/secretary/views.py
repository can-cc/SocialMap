from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.contrib.auth.models import AnonymousUser
from userManager.models import UserInformation

class Hello(APIView):
    permission_classes = (permissions.AllowAny, )
    def get(self, request, format=None):
        if isinstance(request.user, AnonymousUser):
            return Response(0)
        else:
            return Response({'username': request.user.username})

class HasInfo(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    def get(self, request, format=None):
        try:
            UserInformation.objects.get(user=request.user)
            return Response({'hasInfo': 1})
        except:
            return Response({'hasInfo': 0})

class Home(APIView):
    permission_classes = (permissions.AllowAny, )
    def get(self, request, format=None):
        return Response('welcome, but you can not do anything with non-api!')