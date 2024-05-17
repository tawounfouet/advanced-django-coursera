# Optimizing Django Rest Framework: Question 1

## Question 1
Add caching to the Post list endpoint, for 60 seconds. While this question won’t fail if you don’t use the vary-on decorators, later questions will, so make sure you use them.
TRY IT

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
        return super(PostViewSet, self).get_queryset()

    # Question 1: Make changes to this class

    @method_decorator(cache_page(60))
    @method_decorator(vary_on_headers("Authorization"))
    @method_decorator(vary_on_cookie)
    def list(self, *args, **kwargs):
        return super(PostViewSet, self).list(*args, **kwargs)
```

- Import method_decorator, cache_page, vary_on_headers, and vary_on_cookie
- Cache the page for 60 seconds
- Vary on headers
- Vary on cookies
- Define list method