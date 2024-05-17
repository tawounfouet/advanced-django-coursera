from django_filters import rest_framework as filters

# Question 2: Add imports you need here

from assessment.models import Post


class PostFilterSet(filters.FilterSet):
    # Questions 2 and 3: Implement the class body
    class Meta:
        model = Post
        fields = ["author", "slug"]