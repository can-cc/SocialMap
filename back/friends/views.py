from django.shortcuts import render
from django.contrib.auth.models import User
from userManager.serializers import *
from rest_framework import mixins
from rest_framework import generics
from django.http import Http404, HttpResponseBadRequest, HttpResponseServerError
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from .models import *
from .serializers import UserFriendSerialize
from .FriendUtil import *

class FriendOperating(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    def get(self, request, username, format=None):
        user = request.user
        try:
            friends = UserFriends.objects.get(user=user, friend=username)
            serializer = UserFriendSerialize(friends)
            return Response(serializer.data)
        except:
            raise Http404

    def post(self, request, format=None):
        try:
            wtafName = request.data['wtafName']
        except:
            raise HttpResponseBadRequest
        try:
            wta = User.Objects.get(username=wtafName)
            makeFriend(request.user, wta)
            return Response(1)
        except:
            raise HttpResponseServerError

    def put(self, request, format=None):
        pass

    def delete(self, request, format=None):
        try:
            wtdfName = request.data['wtdfName']
        except:
            raise HttpResponseBadRequest
        try:
            wtd = User.Objects.get(username=wtdfName)
            deleteFriend(request.user, wtd)
            return Response(1)
        except:
            raise HttpResponseServerError

class MakeFriendOperating(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    #see himself all request
    def get(self, request, format=None):
        pass

    #make friend request
    def post(self, request, format=None):
        try:
            wtmfName = request.data['wtmfName']
        except:
            raise HttpResponseBadRequest
        try:
            wtb = User.Objects.get(username=wtmfName)
            askMakeFriend(request.user, wtb)
            return Response(1)
        except:
            raise HttpResponseServerError

    def delete(self, request, format=None):
        pass

class UserFriendsList(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    def get(self, request, format=None):
        user = request.user
        try:
            friends = UserFriends.objects.get(user=user)
            serializer = UserFriendSerialize(friends, many=True)
            return Response(serializer.data)
        except:
            raise Http404

class FriendRequestion(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    #get all
    def get(self, request, format=None):
        pass

    #accept or Reject
    def put(self, request, format=None):
        pass