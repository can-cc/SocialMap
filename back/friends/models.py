from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserFriends(models.Model):
    user = models.ForeignKey(User, related_name="userFriend")
    friend = models.ForeignKey(User)
    IsHidden = models.BooleanField(default=False)
    Friendliness = models.IntegerField(default=1)#Intimacy
    DateCreated = models.DateField(auto_now_add=True)

class UserAskFriends(models.Model):
    user = models.ForeignKey(User, related_name="askMF")
    wtm = models.ForeignKey(User)
    stats = models.IntegerField()
    askDate = models.DateField(auto_now_add=True)

class FriendsCategories(models.Model):
    pass

class FriendsInUserCategories(models.Model):
    pass
