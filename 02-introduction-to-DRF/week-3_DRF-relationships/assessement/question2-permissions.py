# permissions.py
from rest_framework.permissions import BasePermission, SAFE_METHODS


class InversePermissions(BasePermission):
    # Question 2: Implement your permission methods
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return not request.user.is_anonymous

        return request.user.is_anonymous

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return not request.user.is_anonymous

        return request.user.is_anonymous