__author__ = 'tyan'
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from userManager.models import UserInformation

# Create your models here.
class MarkPosts(models.Model):
    user = models.ForeignKey(User, related_name='marks')
    userInfo = models.ForeignKey(UserInformation, related_name='information')
    title = models.CharField(max_length=50)
    text = models.TextField()
    picture = models.ImageField(blank=True, null=True)
    postTime = models.DateTimeField(auto_now_add=True)
    point = models.PointField(srid=32140)
    accuracy = models.FloatField(blank=True, null=True)
    postTpye = models.IntegerField(blank=True, null=True)#Todo not blank
    liveTime = models.IntegerField(blank=True, null=True)
    objects = models.GeoManager()