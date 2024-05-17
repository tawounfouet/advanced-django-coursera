from django.db import models
from django.conf import settings

# Question 1: Add your imports for generic relationships below
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class Comment(models.Model):
    content = models.TextField()
    # Question 1: Add your fields for generic relationships below
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()


class Thing(models.Model):
    name = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    # Question 1: Add your fields for generic relationships below
    comments = GenericRelation(Comment)