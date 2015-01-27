__author__ = 'tyan'
from rest_framework import permissions

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, user):
        return user == request.user

class IsNotLogin(permissions.BasePermission):
    def has_permission(self, request, view):
        print request.user
        if request.user == None:
            return False
        return True