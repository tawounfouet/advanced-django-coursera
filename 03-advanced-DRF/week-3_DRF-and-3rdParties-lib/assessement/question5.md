# Django Rest Framework and Third-Party Libraries: Question 5

## Question 5

An image field has been set up on the Post model as a VersatileImageField. We want to be able to expose two sizes in the serialized response:
full_size, which is the original URL of the image.
thumbnail, which is a 200 x 200 thumbnail.
Make changes to PostSerializer in assessment/serializers.py to enable these sizes. You’ll need to add an import to the file too.


## Task

```python
from rest_framework import serializers

from assessment.models import Post


# Question 5: Add your import here


class PostSerializer(serializers.ModelSerializer):
    # Question 5: Make changes to this class

    class Meta:
        model = Post
        fields = "__all__"
```


## Solution

```python
from rest_framework import serializers

# Question 5: Add your import here
from versatileimagefield.serializers import VersatileImageFieldSerializer

from assessment.models import Post


class PostSerializer(serializers.ModelSerializer):
    # Question 5: Make changes to this class
    image = VersatileImageFieldSerializer(
        sizes=[
            ("full_size", "url"),
            ("thumbnail", "thumbnail__200x200"),
        ],
        read_only=True,
    )

    class Meta:
        model = Post
        fields = "__all__"
```

- Import VersatileImageFieldSerializer.
- Create the image attribute which is a VersatileImageFieldSerializer.
- Pass it the argument size which is a list of tuples.
- One tuple should be ("full_size", "url") which sets the size full_size to the image itself.
- The other tuple should be ("thumbnail", "thumbnail__200x200") which sets the size thumbnail to the image resized to 200 pixels by 200 pixels.