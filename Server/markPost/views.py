__author__ = 'tyan'
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .serializers import MarkPostSerializers, PostMarkSerializers, AreaMarkPostSerializers, MarkPostBubbleSerializers, CommentSerializers
from .models import MarkPosts, Comment
from .permissions import IsOwnerOrReadOnly
from django.http import Http404
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from django.contrib.gis.geos import *
from rest_framework import generics
from django.contrib.gis.measure import D

#Todo: Throttling
class MarkPostDetail(APIView):
    def getObject(self, pk):
        try:
            return MarkPosts.objects.get(pk=pk)
        except MarkPosts.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        mark = self.getObject(pk)
        serializer = MarkPostSerializers(mark)
        return Response(serializer.data)

class MarkPostList(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    def post(self, request, format=None):
        import copy
        data = {}
        data['user'] = request.user.pk
        data['userInfo'] = request.user.pk
        data['accuracy'] = request.data['accuracy']
        data['text'] = request.data['text']
        data['title'] = request.data['title']
        if request.data['picture'] != 'undefined':
            data['picture'] = request.data['picture']
        print request.data['picture']
        print type(request.data['picture'])
        print type(data['picture'])
        data['title'] = request.data['title']
        position = request.data['point']
        position.replace('+', ' ')
        data['point'] = fromstr('POINT(' + position + ')')
        # data['point'] = fromstr('POINT(' + position + ')')# srid=4326)
        serializer = PostMarkSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#deprecated
class AreaMarkPosts(APIView):
    def get(self, request, position, format=None):
        position = 'POINT(' + position + ')'
        position.replace('+', ' ')
        pnt = position
        qs = MarkPosts.objects.filter(point__distance_lte=(pnt, 700000))
        serializer = MarkPostSerializers(qs, many=True)
        return Response(serializer.data)

class AreaMarkBubblePosts(APIView):
    def get(self, request, position, format=None):
        position = 'POINT(' + position + ')'
        position.replace('+', ' ')
        pnt = position
        qs = MarkPosts.objects.filter(point__distance_lte=(pnt, 700000))
        serializer = MarkPostBubbleSerializers(qs, many=True)
        return Response(serializer.data)

class UesrAllMarkPost(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    def get(self, request, format=None):
        user = request.user
        qs = MarkPosts.objects.filter(user=user, valid=True)
        serializer = MarkPostSerializers(qs, many=True)
        return Response(serializer.data)

class CommitList(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    def get(self, request, pk, format=None):
        try:
            markPost = MarkPosts.objects.get(pk=pk)
        except:
            raise Http404
        comments = Comment.objects.filter(markPosts=markPost)
        serializer = CommentSerializers(comments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CommentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommitDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly, )
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers