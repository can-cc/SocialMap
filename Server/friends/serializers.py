__author__ = 'tyan'
from django.contrib.auth.models import User
from rest_framework import serializers
from userManager.models import UserInformation
from userManager.serializers import UserSimpleShowSerializer, UserRelationInfoShowSerializer
from .models import UserFriends, UserFollows
from userManager.serializers import UserRelationInfoShowSerializer

class UserFriendSerialize(serializers.ModelSerializer):
    friends = UserRelationInfoShowSerializer()
    class Meta:
        model = UserFriends
        fields = ('friend', 'Friendliness')

###############################################################################################


class UserFollowsSerialize(serializers.ModelSerializer):
    follow = UserRelationInfoShowSerializer()

    class Meta:
        model = UserFollows
        fields = ('id', 'user', 'follow', )
#todo
class UserFollowersSerialize(serializers.ModelSerializer):
    user = UserRelationInfoShowSerializer()

    class Meta:
        model = UserFollows
        fields = ('id', 'user', 'follow')
