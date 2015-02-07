from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from .models import ChinaCity
from .serializers import ChinaCitySerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions

class ChinaCityQuery(APIView):
    permission_classes = (permissions.AllowAny, )
    def getCityObj(self, position):
        print position
        #try:
        return ChinaCity.objects.filter(geom__contains=position)[0]
        #except:
            #raise Http404
    def get(self, request, position, format=None):
        position = 'POINT(' + position + ')'
        city = self.getCityObj(position)
        return Response( ChinaCitySerializer(city).data )

