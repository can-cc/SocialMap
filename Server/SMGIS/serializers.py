__author__ = 'tyan'
from rest_framework import serializers
from .models import ChinaCity

class ChinaCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChinaCity
        fields = ('name_2',)