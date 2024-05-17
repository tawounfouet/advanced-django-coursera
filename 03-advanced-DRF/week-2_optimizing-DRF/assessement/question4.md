# Optimizing Django Rest Framework: Question 4

## Question 4
We want to vary the Posts that are shown based on the User that’s logged in. For anonymous users, all Posts should be returned. For a logged-in user, they should only see the Posts of which they are an author. You’ll need to make changes to PostViewSet to do this. Make sure this applies to the detail view as well.

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
        if self.request.user.is_anonymous:
            return queryset

        return queryset.filter(author=self.request.user)

    # Question 1: Make changes to this class

    @method_decorator(cache_page(60))
    @method_decorator(vary_on_headers("Authorization"))
    @method_decorator(vary_on_cookie)
    def list(self, *args, **kwargs):
        return super(PostViewSet, self).list(*args, **kwargs)
```

- Create queryset and set its value to all posts
- If the user is anonymous, return queryset
- If the user is logged-in, return all the posts filtered by author=self.request.user so only those posts authored by the user are returned