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

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        # Write permissions are only allowed to the owner of the snippet.
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user