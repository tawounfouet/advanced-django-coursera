## Django Rest Framework and Third-Party Libraries: Question 2

## Question 2
We want to add filtering of posts by author or slug, using an exact match. A PostFilterSet class has been set up in assessment/filters.py. Implement the class body to allow this filtering, then make changes to PostViewSet to use it. You’ll also need to add a setting in settings.py.
Use the tabs in the IDE (left) to select the file you want to modify.



```python
# settings.py

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        # Question 4: Add your settings here
        
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly"
    ],
    # Question 1: Add your setting here
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    # Question 2: Add your setting here
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}
```
Set the the default filter backend to the DRF filter backend.



```python
# filter.py

from django_filters import rest_framework as filters

# Question 2: Add imports you need here

from assessment.models import Post


class PostFilterSet(filters.FilterSet):
    # Questions 2 and 3: Implement the class body
    class Meta:
        model = Post
        fields = ["author", "slug"]
```
- Import the Post model.
- In the PostFilterSet class, create the Meta class.
- Create the Model field and set it to Post.
- Set fields to the list of "author" and "slug".


```python
# views.py

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from assessment.models import Post
from assessment.serializers import PostSerializer

# Question 2: Add any imports you need here

from assessment.filters import PostFilterSet


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # Question 2: Update this class to use your filterset
    filterset_class = PostFilterSet

    def get_queryset(self):
        queryset = super(PostViewSet, self).get_queryset()
        if self.request.user.is_anonymous or self.request.GET.get("all") == "true":
            return queryset

        return queryset.filter(author=self.request.user)


# No changes are required to this class
class WhoAmIView(APIView):
    def get(self, request):
        return Response(
            {"username": None if request.user.is_anonymous else request.user.username}
        )
```
- Import the PostFilterSet class.
- Create the filterset_class attribute and set it to PostFilterSet.