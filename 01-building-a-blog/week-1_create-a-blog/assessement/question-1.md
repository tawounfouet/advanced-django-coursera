# Question 1
We’ve scaffolded two models for the assessment app: Thing, and Comment. A Thing can represent anything! It just a name. A Comment can be added to a Thing. Like the Comment model in Blango, they will be mapped together using a generic relationship.

You will need to edit assessment/models.py and make the following changes:
- Add the fields necessary to create a generic relationship to the Comment model
- Add a comments attribute to Thing with a GenericRelation, which will enable fetching of comments for a Thing
- Make sure to import all the necessary classes

**Important**: After making your changes, you’ll need to run makemigrations and migrate before running the unit tests.

```python
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
```

### Imports
- Import GenericForeignKey and GenericRelation from django.contrib.contenttypes.fields
- Import ContentType from django.contrib.contenttypes.models

### Comment Model
- Assign a ForeignKey to content_type
- Set object_id to a positive integer field
- Assign a GenericForeignKey to content_object

### Thing Model
Create a generic relationship with comments


