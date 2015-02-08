from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import generics
from .models import UsersMessage
from django.contrib.auth.models import User
from .serializers import *


class SenderMessageList(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    def get(self, request, format=None):
        user = request.user
        messages = UsersMessage.objects.filter(sender=user)
        serializer = Message2SenderSerialize(messages, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        request.data['sender'] = str(request.user.id)
        serializer = Message2SenderSerialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



