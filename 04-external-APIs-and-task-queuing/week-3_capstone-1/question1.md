# Capstone Part 1: Question 1

## Question 1
The movienight_auth app has been set up with a User model that is intended to be used for authentication with this project. The AUTH_USER_MODEL setting has already been configured appropriately but there are a few attributes on the User model that need to be set. We want to disable the username of the model and instead use email for authentication.

These attributes on the User model need to be set/overridden:
- username
- email
- objects (MovieNightUserManager has already been created)
- USERNAME_FIELD
- REQUIRED_FIELDS

While it’s not required, setting the __str__() method on the model can be useful too:
```py
 def __str__(self):
    return self.email
```

After making these changes you will need to make the migrations before running the tests.
- MAKEMIGRATIONS
- MIGRATE

Expected Output
Your code should pass all of the unit tests.


## Task
```py
from django.contrib.auth.models import AbstractUser, UserManager


class MovieNightUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    pass

```

## Solution
```py
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class MovieNightUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(
        _("email address"),
        unique=True,
    )

    objects = MovieNightUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
```

- Import models from django.db
- Import gettext_lazy from django.utils.translation
- Set username to None
- Set email to an email field. This should be a unique identifier.
- Set objects to MovieNightUserManager() which is already defined in the same file.
- Use the email address for USERNAME_FIELD.
- Set REQUIRED_FIELDS to an empty list.
- It is helpful to define the __str__ method so users can print a string representation of the object.