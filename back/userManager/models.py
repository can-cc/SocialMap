__author__ = 'tyan'
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# class UserShowInformation(models.Model):
#     user = models.OneToOneField(User, related_name="show")
#     NickName = models.CharField(max_length=20)
#     PersonalDescription = models.TextField(blank=True)
#     country = models.IntegerField(blank=True)
#     province = models.IntegerField(blank=True)
#     city = models.IntegerField(blank=True)
#     gender = models.IntegerField(blank=True)
#     birthday = models.IntegerField(blank=True)
#     school = models.CharField(blank=True, max_length=50)
#     schoolId = models.IntegerField(blank=True)
#     interest = models.IntegerField(blank=True)
#     cardId = models.BigIntegerField(blank=True)
#     nowCity = models.IntegerField(blank=True)
#     publicMail = models.EmailField(blank=True)
#     PublicPhoneNumber = models.BigIntegerField(blank=True)
#     QQ = models.BigIntegerField(blank=True)

class Interesting(models.Model):
    category = models.CharField(max_length=50, default='default', blank=True)
    interesting = models.CharField(max_length=50, blank=True, null=True)

# class UserInformation(models.Model):
#     pass
#Todo: create index
class UserInformation(models.Model):
    user = models.OneToOneField(User, related_name="information")
    nickName = models.CharField(max_length=20, unique=True)
    portrait = models.ImageField(blank=True, null=True)
    personalDescription = models.TextField(blank=True, null=True)
    phoneNumber = models.BigIntegerField(blank=True, null=True)
    country = models.IntegerField(blank=True, null=True)
    province = models.IntegerField(blank=True, null=True)
    city = models.IntegerField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    school = models.CharField(max_length=50, blank=True, null=True)
    schoolId = models.IntegerField(blank=True, null=True)
    cardId = models.BigIntegerField(blank=True, null=True)
    nowCity = models.IntegerField(blank=True, null=True)
    publicMail = models.EmailField(blank=True, null=True)
    publicPhoneNumber = models.BigIntegerField(blank=True, null=True)
    QQ = models.BigIntegerField(blank=True, null=True)
    lastIp = models.IPAddressField(blank=True, null=True)
    lastActivity = models.TimeField(blank=True, null=True)
    userType = models.IntegerField(blank=True, null=True)
    loginTimes = models.IntegerField(default=1)
    hitTimes = models.IntegerField(default=0)
    activityScore = models.IntegerField(default=0)
    friendCount = models.IntegerField(default=0)
    interest = models.ManyToManyField(Interesting, through='UserInteresting', through_fields=('userInfo', 'interesting'), blank=True, null=True)

class UserInteresting(models.Model):
    userInfo = models.ForeignKey(UserInformation)
    interesting = models.ForeignKey(Interesting)

class UserInformationDisplay(models.Model):
    user = models.OneToOneField(User, related_name="infoDispaly")
    personalDescription = models.TextField(blank=True)
    phoneNumber = models.BooleanField(default=True)
    country = models.BooleanField(default=True)
    province = models.BooleanField(default=True)
    city = models.BooleanField(default=True)
    birthday = models.BooleanField(default=True)
    school = models.BooleanField(default=True)
    schoolId = models.BooleanField(default=True)
    interest = models.BooleanField(default=True)
    cardId = models.BooleanField(default=False)
    nowCity = models.BooleanField(default=True)
    publicMail = models.BooleanField(default=True)
    publicPhoneNumber = models.BooleanField(default=True)
    QQ = models.BooleanField(default=True)
    userType = models.BooleanField(default=True)
    friendCount = models.BooleanField(default=True)


# class UserBackInformation(models.Model):
#     lastIp = models.IPAddressField(blank=True)
#     LastActivity = models.TimeField(blank=True)
#     UserType = models.IntegerField(blank=True)
#     loginTimes = models.IntegerField(default=1)
#     hitTimes = models.IntegerField(default=0)
#     activityScore = models.IntegerField(default=0)

class UserSecurity(models.Model):
    user = models.OneToOneField(User)
    isLock = models.BooleanField(default=False)
    LoginFailTime = models.IntegerField(default=0)
    PasswordQuestion1 = models.CharField(blank=True, null=True, max_length=50)
    PasswordAnswer1 = models.CharField(blank=True, null=True, max_length=50)
    PasswordQuestion2 = models.CharField(blank=True, null=True, max_length=50)
    PasswordAnswer2 = models.CharField(blank=True, null=True, max_length=50)
    PasswordQuestion3 = models.CharField(blank=True, null=True, max_length=50)
    PasswordAnswer3 = models.CharField(blank=True, null=True, max_length=50)




