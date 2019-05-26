from rest_framework import permissions


class IsGetOrAuthenticated(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        methods = ('GET', 'HEAD', 'OPTIONS')

        if request.method in methods:
            return True

        return obj.id == request.user.id
