__author__ = 'tyan'

from rest_framework import serializers
from userManager.models import UserInformation
from .models import MarkPosts, Comment
from userManager.serializers import UserSimpleShowSerializer, PortraitSerializer, UserRelationInfoShowSerializer


class MarkPostSerializers(serializers.ModelSerializer):
    userInfo = UserSimpleShowSerializer()
    title = serializers.CharField()
    text = serializers.CharField()
    picture = serializers.ImageField(required=False)
    point = serializers.CharField()
    postTpye = serializers.IntegerField(required=False)

    def create(self, validated_data):
        return MarkPosts.objects.create(**validated_data)

    class Meta:
        model = MarkPosts
        fields = ('id', 'userInfo', 'title', 'text', 'picture','postTime', 'point', 'postTpye')

#show bubble message on map
class MarkPostBubbleSerializers(serializers.ModelSerializer):
    userInfo = PortraitSerializer()
    class Meta:
        model = MarkPosts
        fields = ('id', 'userInfo', 'point')

class AreaMarkPostSerializers(serializers.ModelSerializer):
    title = serializers.CharField()
    text = serializers.CharField()
    picture = serializers.ImageField(required=False)
    point = serializers.CharField()
    postTpye = serializers.IntegerField(required=False)

    class Meta:
        model = MarkPosts
        fields = ('title', 'text', 'picture','postTime', 'point', 'postTpye')

#show user all markPost
#related serializer
class UserMarkSerializers(serializers.ModelSerializer):
    marks = serializers.StringRelatedField(many=True)

    class Meta:
        model = UserInformation
        fields = ('nickName', 'portrait', 'marks')

class PostMarkSerializers(serializers.ModelSerializer):
    title = serializers.CharField()
    text = serializers.CharField()
    picture = serializers.ImageField(required=False)
    point = serializers.CharField()
    postTpye = serializers.IntegerField(required=False)
    def create(self, validated_data):
        return MarkPosts.objects.create(**validated_data)

    class Meta:
        model = MarkPosts
        fields = ('user', 'userInfo', 'title', 'text', 'picture', 'postTime', 'point', 'postTpye')

class PostMarkPrimaryKeySerializers(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = MarkPosts
        fields = ('id', )

class CommentSerializers(serializers.ModelSerializer):
    markPosts = PostMarkPrimaryKeySerializers()
    user = UserRelationInfoShowSerializer(read_only=True)
    text = serializers.CharField()

    def create(self, validated_data):
        return MarkPosts.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance
    class Meta:
        model = Comment
        fields = ('id', 'markPosts', 'user', 'text', 'time')