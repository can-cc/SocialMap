__author__ = 'tyan'
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .serializers import MarkPostSerializers, PostMarkSerializers, AreaMarkPostSerializers
from .models import MarkPosts
from django.http import Http404
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from django.contrib.gis.geos import *
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
        data = copy.deepcopy(request.data)
        data = eval(str(data))
        data['user'] = request.user.pk
        data['userInfo'] = request.user.pk
        position = data['point']
        position.replace('+', ' ')
        data['point'] = fromstr('POINT(' + position + ')', srid=4326)
        serializer = PostMarkSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AreaMarkPosts(APIView):
    def get(self, request, position, format=None):
        position = 'POINT(' + position + ')'
        position.replace('+', ' ')
        pnt = position
        qs = MarkPosts.objects.filter(point__distance_lte=(pnt, 700000))
        serializer = MarkPostSerializers(qs, many=True)
        return Response(serializer.data)

class UesrAllMarkPost(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    def get(self, request, pk, format=None):
        user = User.objects.get(pk=pk)
        qs = MarkPosts.objects.filter(user=user)
        serializer = MarkPostSerializers(qs, many=True)
        return Response(serializer.data)