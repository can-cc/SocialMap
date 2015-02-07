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
from .serializers import UserFriendSerialize, UserFollowsSerialize, UserFollowersSerialize
from .FriendUtil import *
from userManager.permissions import IsOwner

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


###############################################################################################
#above  models is deprecated(Abandoned)

#Todo : Permission has not been tested


class UserFollowsList(APIView):
    def get(self, request, format=None):
        permission_classes = (permissions.IsAuthenticated, )
        user = request.user
        follows = UserFollows.objects.filter(user=user)
        serializer = UserFollowsSerialize(follows, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        permission_classes = (permissions.IsAuthenticated, IsOwner )
        followId = int(request.data['followId'])
        user = request.user
        try:
            follow = User.objects.get(id=followId)
        except:
            return Response({'follow': followId}, status=status.HTTP_404_NOT_FOUND)
        try:
            userFollow = UserFollows(user=user, follow=follow)
            userFollow.save()
            return Response({'user': user.id,
                             'follow': followId}, status=status.HTTP_201_CREATED)
        except:
            #todo: unique ? 400?
            return Response({'error': 'HTTP_400_BAD_REQUEST'}, status=status.HTTP_400_BAD_REQUEST)


class UserFollowsDetail(APIView):
    permission_classes = (permissions.IsAuthenticated, IsOwner )
    def get(self, request, pk, format=None):
        userFollow = UserFollows(id=pk)
        serializer = UserFollowsSerialize(userFollow)
        return Response(serializer.data)

    #9.7 DELETE
    #A successful response SHOULD be 200 (OK)
    # if the response includes an entity describing the status,
    # 202 (Accepted) if the action has not yet been enacted,
    # or 204 (No Content) if the action has been enacted but the response does not include an entity.
    def delete(self, request, pk, format=None):
        followId = pk
        user = request.user
        try:
            userFollow = UserFollows.objects.get(id=pk)
        except:
            return Response({'follow': followId}, status=status.HTTP_404_NOT_FOUND)
        try:
            userFollow.delete()
            return Response({'user': user.id,
                             'follow': followId}, status=status.HTTP_200_OK)
        except:
            return Response({'user': user.id,
                             'follow': followId}, status=status.HTTP_400_BAD_REQUEST)

class UserFollowersList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = UserFollowers.objects.all()
    serializer_class = UserFollowersSerialize

class UserFollowersDetail(generics.RetrieveDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwner )
    queryset = UserFollowers.objects.all()
    serializer_class = UserFollowersSerialize



