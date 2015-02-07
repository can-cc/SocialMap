__author__ = 'tyan'
from rest_framework import serializers
from .models import UserTrack

class UserTrackList(serializers.ModelSerializer):
    footPoint = serializers.CharField()
    accuracy = serializers.FloatField()
    stayLong = serializers.TimeField(required=False)

    def create(self, validated_data):
        return UserTrack.objects.create(**validated_data)

    class Meta:
        model = UserTrack
        fields = ('user', 'footPoint', 'accuracy', 'stayLong')