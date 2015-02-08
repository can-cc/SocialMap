__author__ = 'tyan'
from rest_framework import permissions

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']
class AllowRemoveFollower(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.follow == request.user

class AllowRemoveFollow(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
