from rest_framework import permissions


class IsGetOrAuthenticated(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        METHODS = ('GET', 'HEAD', 'OPTIONS', 'POST')

        if request.method in METHODS:
            return True

        return obj.id == request.user.id
