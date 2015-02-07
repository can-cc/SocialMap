from django.shortcuts import render
from django.contrib.auth.models import User
from userManager.serializers import *
from rest_framework import mixins
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *
from .models import *
from MySQLdb import IntegrityError

class UserTrackView(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    def post(self, request, format=None):
        userPk = request.user.pk
        import copy
        data = copy.deepcopy(request.data)
        data = eval(str(data))
        data['user'] = userPk
        position = data['footPoint']
        position = position.replace('+', ' ')
        data['footPoint'] = 'POINT(' + position + ')'
        serializer = UserTrackList(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(1, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
