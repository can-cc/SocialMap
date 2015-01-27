__author__ = 'tyan'
from django.contrib.auth.models import User
from rest_framework import serializers
from userManager.models import UserInformation
from userManager.serializers import UserSimpleShowSerializer, UserRelationInfoShowSerializer
from .models import UserFriends

class UserFriendSerialize(serializers.ModelSerializer):
    friends = UserRelationInfoShowSerializer()
    class Meta:
        model = UserFriends
        fields = ('friend', 'Friendliness')