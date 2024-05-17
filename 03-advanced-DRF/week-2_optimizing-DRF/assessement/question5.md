# Optimizing Django Rest Framework: Question 5

## Question 5
We want to give logged-in users the option of viewing all Posts. They’ll be able to do this by adding ?all=true to the URL, both list and detail. For example, /api/v1/posts/?all=true should get all Posts even if a user is logged in. Likewise, the same argument can be appended to the detail view so a logged-in user can retrieve a Post that they’d otherwise not be able to.


## Task

```python
# Question 1: Add imports
from rest_framework import viewsets

from assessment.models import Post
from assessment.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        # Questions 4 & 5: Update this method
        return super(PostViewSet, self).get_queryset()

    # Question 1: Make changes to this class
```


## Solution

```python
# Question 1: Add imports
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers, vary_on_cookie
from rest_framework import viewsets

from assessment.models import Post
from assessment.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        # Questions 4 & 5: Update this method
        queryset = super(PostViewSet, self).get_queryset()
        if self.request.user.is_anonymous or self.request.GET.get("all") == "true":
            return queryset

        return queryset.filter(author=self.request.user)

    # Question 1: Make changes to this class

    @method_decorator(cache_page(60))
    @method_decorator(vary_on_headers("Authorization"))
    @method_decorator(vary_on_cookie)
    def list(self, *args, **kwargs):
        return super(PostViewSet, self).list(*args, **kwargs)
```

Alter the conditional so that all posts are returned if the user is anonymous or if the URL asks for all posts