__author__ = 'tyan'
from .models import UserFriends, UserAskFriends
def askMakeFriend(asker, wtm):
    UserAskFriends.objects.create(user=asker, wtm=wtm)


def makeFriend(asker, wta):
    UserFriends.objects.create(user=asker, friend=wta)

def deleteFriend(asker, wtd):
    UserFriends.objects.delete(user=asker, friend=wtd)