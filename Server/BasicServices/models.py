from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class SysMessage(models.Model):
    pass

class UsersMessage(models.Model):
    sender = models.ForeignKey(User, related_name='sendMessage',)
    receiver = models.ForeignKey(User, related_name='receiveMessage',)
    title = models.CharField(max_length=100,)
    text = models.TextField(max_length=100,)
    time = models.DateTimeField(auto_now_add=True)
    type = models.IntegerField(default=1)