# Advanced Django Authentication: Question 2

## Question 2
A Profile class has been scaffolded with a single attribute. Add a field to relate it to the User model, making sure to create the relationship in a flexible manner. The names of the attributes should be user on the Profile and profile on the User. You will need to run manage.py makemigrations and manage.py migrate to apply your changes to the database.

## Default Field Value
`Note that if you’re prompted to enter a default field value during the makemigrations process, it’s OK to just select 1, then type None and press Enter on the keyboard`


## Problem
```python
from django.contrib.auth.models import AbstractUser
from django.db import models

# Question 2: Add imports you need here


class User(AbstractUser):
    # This class does not need to be edited
    pass


class Profile(models.Model):
    location = models.TextField()
    # Question 2: Add the field(s) to link a profile to the User
```


## Solution

```python
from django.contrib.auth.models import AbstractUser
from django.db import models

# Question 2: Add imports you need here
from django.conf import settings

class User(AbstractUser):
    # This class does not need to be edited
    pass


class Profile(models.Model):
    location = models.TextField()
    # Question 2: Add the field(s) to link a profile to the User
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```


- Import settings from django.conf
- Create the user field


## Solution 2

```python
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Question 2: Add imports you need here
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    # This class does not need to be edited
    pass

class Profile(models.Model):
    location = models.TextField()
    # Question 2: Add the field(s) to link a profile to the User
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)  # Temporary default value

# Signal to create or update user profile
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()

```