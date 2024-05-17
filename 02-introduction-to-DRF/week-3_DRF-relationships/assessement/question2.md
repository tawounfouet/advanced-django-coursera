# Django Rest Framework Relationships: Question 2

## Question 2
A basic API view has been set up in bakery/api/views.py called NameAndCountView. It supports GET (for list and detail), POST, PUT and DELETE methods, although it doesn’t persist any data (these methods have been implemented on NameAndCountBaseView so they are not a distraction for this question). The view is mapped by the /api/v1/name-and-count/ and /api/v1/name-and-count/<pk> URLs.

You’ll need to update this view so it uses the InversePermissions class to control access to it.

As well as that, you’ll need to actually implement permissions methods on the InversePermissions class (has_permission() and has_object_permission()). This permissions class should behave in the inverse of what we expect, that is:
- unauthenticated users should be able to create, update and delete objects, but not retrieve or list them
- authenticated users can list or retrieve objects but can’t create, update or delete
It’s a strange use case, for sure, but will make sure you understand the permissions system.
To help with testing, the create_fixtures management command creates a user with username testuser and password password that you can test with.


```python
# views.py
from bakery.api.assessment_views import NameAndCountBaseView

# Question 2: Add any imports you need here
from bakery.api.permissions import InversePermissions


class NameAndCountView(NameAndCountBaseView):
    # Question 2: Make changes to this class to configure permissions
    permission_classes = [InversePermissions]
```
- Import InversePermissions
- Set the permission class to InversePermissions


```python
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
```

- Import SAFE_METHODS
- Define has_permission such that it returns the opposite of request.user.is_anonymous if request.method is in SAFE_METHODS
- Define has_object_permission such that it returns the opposite of request.user.is_anonymous if request.method is in SAFE_METHODS