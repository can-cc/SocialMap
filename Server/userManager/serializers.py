__author__ = 'tyan'
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserInformation

#use to login and resiger
class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=False, allow_blank=True, max_length=20)
    last_name = serializers.CharField(required=False, allow_blank=True, max_length=20)
    email = serializers.EmailField(required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'date_joined', 'email')

    def create(self, validated_data):
        rawPassword = validated_data['password']
        validated_data['password'] = ""
        user = User.objects.create(**validated_data)
        user.set_password(rawPassword)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = instance.password
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.first_name)
        instance.set_password(password)
        instance.save()
        return instance

class UserModifySerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False, allow_blank=True, max_length=20)
    last_name = serializers.CharField(required=False, allow_blank=True, max_length=20)

    class Meta:
        model = UserInformation
        fields = ('id', 'password', 'first_name', 'last_name')

    def update(self, instance, validated_data):
        password = instance.password
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.first_name)
        instance.set_password(password)
        instance.save()
        return instance

class UserSimpleShowSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    nickName = serializers.CharField()
    portrait = serializers.ImageField(required=False)
    personalDescription = serializers.CharField(required=False)

    def update(self, instance, validated_data):
            instance.nickName = validated_data.get('nickName', instance.nickName)
            instance.portrait = validated_data.get('portrait', instance.portrait)
            instance.personalDescription = validated_data.get('personalDescription', instance.personalDescription)
            instance.save()
            return instance
    class Meta:
        model = UserInformation
        fields = ('user', 'nickName', 'portrait', 'personalDescription',)

class PortraitSerializer(serializers.ModelSerializer):
    #user = serializers.PrimaryKeyRelatedField(queryset=UserInformation.objects.all())
    portrait = serializers.ImageField(required=False)
    def create(self, validated_data):
        return UserInformation.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.portrait = validated_data.get('portrait', instance.portrait)
        instance.save()
        return instance
    class Meta:
        model = UserInformation
        fields = ('id', 'user', 'portrait', )

class UserShowShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformation
        fields = ('nickName', 'portrait', 'personalDescription')

#common serializer
class UserRelationInfoShowSerializer(serializers.ModelSerializer):
    information = UserSimpleShowSerializer(required=False)
    class Meta:
        model = User
        fields = ('id', 'information')

#use to create
class UserInformationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    nickName = serializers.CharField(required=False)
    portrait = serializers.ImageField(required=False)
    personalDescription = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    phoneNumber = serializers.IntegerField(required=False)
    country = serializers.IntegerField(required=False)
    province = serializers.IntegerField(required=False)
    city = serializers.IntegerField(required=False)
    birthday = serializers.DateField(required=False)
    school = serializers.IntegerField(required=False)
    schoolId = serializers.IntegerField(required=False)
    interest = serializers.StringRelatedField(many=True, required=False, allow_null=True)
    cardId = serializers.IntegerField(required=False)
    nowCity = serializers.IntegerField(required=False)
    publicMail = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    publicPhoneNumber = serializers.IntegerField(required=False)
    QQ = serializers.IntegerField(required=False)
    userType = serializers.IntegerField(required=False)
    loginTimes = serializers.IntegerField(required=False)
    hitTimes = serializers.IntegerField(required=False)
    friendCount = serializers.IntegerField(required=False)

    def create(self, validated_data):
        return UserInformation.objects.create(**validated_data)

    #Todo: something should be read-only
    class Meta:
        model = UserInformation
        fields = ('user',
                  'nickName',
                  'portrait',
                  'personalDescription',
                  'phoneNumber',
                  'country',
                  'province',
                  'city',
                  'birthday',
                  'school',
                  'schoolId',
                  'interest',
                  'cardId',
                  'nowCity',
                  'publicMail',
                  'publicPhoneNumber',
                  'QQ',
                  'userType',
                  'loginTimes',
                  'hitTimes',
                  'friendCount',)

class UserInformationShowSerializer(serializers.ModelSerializer):
    portrait = serializers.CharField(required=False)
    #Todo: something should be read-only
    class Meta:
        model = UserInformation
        fields = (
                  'nickName',
                  'portrait',
                  'personalDescription',
                  'country',
                  'city',
                  'birthday',
                  'school',
                  ####################!!!!!!!!!!!!!!!!!!!!!
                  #todo: 'interest',
                  'nowCity',
                  'publicMail',
                  'publicPhoneNumber',
                  'QQ',
                  'hitTimes',
                  'friendCount',)

class UserSetting(serializers.ModelSerializer):
    pass

#this show in ui
class UserInfoShowSerializer(serializers.ModelSerializer):
    information = UserInformationShowSerializer()
    class Meta:
        model = User
        fields = ('id', 'information', )