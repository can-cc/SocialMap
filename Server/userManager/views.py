from django.shortcuts import render
from django.contrib.auth.models import User
from userManager.serializers import *
from rest_framework import mixins
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .permissions import IsOwner, IsNotLogin, IsOwnerOrReadOnly
from rest_framework import permissions
from .models import *
from MySQLdb import IntegrityError

#login and register
class UserList(APIView):
    permission_classes = (IsNotLogin, )
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#login and register
class UserDetail(APIView):
    #permission_classes = (IsNotLogin, )
    permission_classes = (IsOwner, )
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    # def get(self, request, pk, format=None):
    #     user = self.get_object(pk)
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)

    def put(self, request, format=None):
        pk = request.data['id']        #warning !!!!!!!!!!!!!!!!!!!!!!!!!
        user = self.get_object(pk)
        serializer = UserModifySerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HimSelfDatail(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    def get(self, request, format=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class changePasswd(APIView):
    permission_classes = (permissions.IsAuthenticated, )

class UserInformationDatail(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    def getObject(self, user):
        try:
            return UserInformation.objects.get(user=user)
        except:
            raise Http404

    def checkObject(self, user):
        if UserInformation.objects.check(user=user):
            return True
        else:
            return False

    def get(self, requset, format=None):
        userInfo = self.getObject(requset.user)
        userInfoser = UserInformationSerializer(userInfo)
        return Response(userInfoser.data)

    def post(self, request, format=None):
        permission_classes = (permissions.IsAuthenticated, )
        if self.checkObject(request.user):
            self.put(self, request, format=None)
        else:
            import copy
            data = {}
            for i in request.data.keys():
                if request.data[i] != '':
                    data[i] = request.data[i]
            data['user'] = request.user.pk
            serializer = UserInformationSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, requset, format=None):
        pass


class SimpleUserInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly, )
    queryset = UserInformation.objects.all()
    serializer_class = UserSimpleShowSerializer

#warining !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#todo:notice: return pic path is 127.0.0.1!
class UserPortraitDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly, )
    queryset = UserInformation.objects.all()
    serializer_class = PortraitSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserPortraitList(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = UserInformation.objects.all()
    serializer_class = PortraitSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#warining !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#todo:notice: return pic path is 127.0.0.1!

#this show in ui
class UserInfoShow(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = User.objects.all()
    serializer_class = UserInfoShowSerializer