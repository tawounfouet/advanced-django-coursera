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