__author__ = 'tyan'
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from userManager.models import UserInformation
import datetime

def content_file_name(instance, filename):
    i = filename.rindex('.')
    suffix = filename[i:]
    return '/'.join(['markpost/pic', instance.user.username + '_mpp_' + str(datetime.datetime.now()) + suffix])

class MarkPosts(models.Model):
    user = models.ForeignKey(User, related_name='marks')
    userInfo = models.ForeignKey(UserInformation, related_name='information')
    title = models.CharField(max_length=50)
    text = models.TextField()
    picture = models.ImageField(blank=True, null=True, max_length=100, upload_to=content_file_name)
    postTime = models.DateTimeField(auto_now_add=True)
    point = models.PointField()
    accuracy = models.FloatField(blank=True, null=True)
    postTpye = models.IntegerField(blank=True, null=True)#Todo not blank
    liveTime = models.IntegerField(blank=True, null=True)
    valid = models.BooleanField(default=True)
    objects = models.GeoManager()

class Review(models.Model):
    user = models.ForeignKey(User, related_name='review')
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)