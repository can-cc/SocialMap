from django.db import models
from django.contrib.gis.db import models as gisModels
from django.contrib.auth.models import User

class UserTrack(gisModels.Model):
    user = gisModels.ForeignKey(User, related_name='Track')
    footPoint = gisModels.PointField()
    accuracy = gisModels.FloatField(blank=True, null=True)
    time = gisModels.DateTimeField(auto_now_add=True)
    stayLong = gisModels.TimeField(blank=True, null=True)
    objects = gisModels.GeoManager()