__author__ = 'tyan'
from rest_framework import serializers
from userManager.serializers import UserRelationInfoShowSerializer
from .models import UsersMessage
from django.contrib.auth.models import User

class Message2SenderSerialize(serializers.ModelSerializer):
    sender = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    receiver = UserRelationInfoShowSerializer(required=False)
    title = serializers.CharField()
    text = serializers.CharField()


    class Meta:
        model = UsersMessage
        fields = ('id', 'sender', 'receiver', 'title', 'text', 'time', 'type', )

class Message2ReceiverSerialize(serializers.ModelSerializer):
    sender = UserRelationInfoShowSerializer()
    receiver = serializers.PrimaryKeyRelatedField(read_only=True)
    title = serializers.CharField()
    text = serializers.CharField()

    def create(self, validated_data):
        return UsersMessage.objects.create(**validated_data)

    class Meta:
        model = UsersMessage
        fields = ('id', 'sender', 'receiver', 'title', 'text', 'time', 'type', )
