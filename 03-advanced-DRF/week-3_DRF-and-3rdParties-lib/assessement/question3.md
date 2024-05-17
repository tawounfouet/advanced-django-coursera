# Django Rest Framework and Third-Party Libraries: Question 3

## Question 3
The API should allow searching for Post content in a case insensitive manner. Implement this filtering on the PostFilterSet. The query parameter should be just content. You won’t have to make changes to PostViewSet, just PostFilterSet.

## Task
```python
from django_filters import rest_framework as filters

# Question 2: Add imports you need here


class PostFilterSet(filters.FilterSet):
    # Questions 2 and 3: Implement the class body
    pass
```

## Solution
```python
from django_filters import rest_framework as filters

# Question 2: Add imports you need here

from assessment.models import Post


class PostFilterSet(filters.FilterSet):
    # Questions 2 and 3: Implement the class body
    content = filters.CharFilter(
        field_name="content",
        lookup_expr="icontains",
    )

    class Meta:
        model = Post
        fields = ["author", "slug"]
``` 

- Add the content attribute to the PostFilterSet class.
- Set its value to filters.CharFilter.
- filters.CharFilter needs the keyword arguments field_name and lookup_expr.
- Their default values should be "content" and "icontains" respectively.