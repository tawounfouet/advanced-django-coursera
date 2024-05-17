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