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