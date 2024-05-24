from rest_framework import permissions


class UserFieldPermission(permissions.BasePermission):
    user_field = None

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Get the "owner" of the object from the user_field
        return getattr(obj, self.user_field) == request.user


class IsCreatorPermission(UserFieldPermission):
    #pass
    # Question 3
    user_field = "creator"


class IsInviteePermission(UserFieldPermission):
    #pass
    # Question 3
    user_field = "invitee"
