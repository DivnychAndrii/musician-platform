from rest_framework.permissions import BasePermission


class IsCreatorOrSender(BasePermission):

    def has_object_permission(self, request, view, obj):

        return request.user == obj.from_user or request.user == obj.to_creator
