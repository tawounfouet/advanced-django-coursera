# Capstone Part 2: Question 2

## Question 2
In this question you’ll make a number of changes to support Django Rest Framework. The first is to configure the settings. Here are the REST_FRAMEWORK settings that we want:

### Settings
- DEFAULT_PERMISSION_CLASSES should be rest_framework.permissions.IsAuthenticated.
- A user should be able to authenticate with BasicAuthentication, SessionAuthentication, TokenAuthentication and JWTAuthentication.
- rest_framework.pagination.PageNumberPagination should be used as the default pagination class.

### Fill in movie details
When fetching a movie detail through the UI, fill_movie_details() is called to populate missing data for the movie. We want the MovieViewSet to do the same thing when fetching the detail for a Movie. Implement the get_object() method and have it also call fill_movie_details().

### Different serializers on MovieNightViewSet
MovieNightViewSet should use different serializers for a create, then for other actions. On create, use MovieNightCreateSerializer, otherwise use MovieNightSerializer, for the serializer class.

### Configure MovieSerializer
MovieSerializer is only partially configured. It should:
- Have a model set
- Return all fields
- All fields must be marked as read-only

### Expected Output
Before checking your work, you will need to create two users. Note, the users from the previous module do not work in this module.
- CREATE SUPERUSER

Then start the dev server and log in as one user and invite the other user to a MovieNight event. With the other user, accept the invitation.
- START DEV SERVER

**View Movie Night**

Open the API and log in using the information you just created.

- View API

Explore the different endpoints to see the information from the MovieNight event you created.

### API endpoints

API endpoints
Here is a list of URLs that have been configured:

- api/v1/auth/login: Standard DRF login and logout views
- api/v1/token-auth/: API view for obtaining a DRF token.
- api/v1/jwt/: For obtaining a JWT.
- api/v1/jwt/refresh/: For refreshing a JWT.
- api/v1/movienight-auth/users/<email>: Get information about a user by email.
- api/v1/movies/movies/<pk>: List Movies or get detail by PK. Note that this endpoint is read-only.
api/v1/movies/movies/search/: Search for Movies, with a term argument provided in the query string. This will call search_and_save() on the term first, before querying the database.
- api/v1/movies/movie-nights/<pk>: List MovieNights or get by PK. The list action will return only MovieNights for which the logged-in user is the creator, however the detail endpoint allows fetching of MovieNights which have either been created by the user, or the user is invited to.
- api/v1/movies/movie-nights/invited/: List MovieNights to which the user has been invited.
- api/v1/movies/movie-nights/<pk>/invite/: POST to this endpoint to invite a user to the MovieNight. Can only be done when authenticated as the creator of the MovieNight. The POST body is JSON with an invitee key, which is the URL to a User object. For example:
```json
{
    "invitee": "http://host/api/v1/movienight-auth/users/ben@example.com"
}
```
- api/v1/movies/movie-night-invitations/<pk>: List MovieNightInvitations, or get detail by PK. Users are only able to access invitations to which they are the invitee. This viewset does not allow creation, instead MovieNightInvitations are created through the invite endpoint on the MovieNight viewset. Only the is_attending flag is writable.
- api/v1/movies/genres/<pk>: List Genres or get by PK.



Your code should pass all of the unit tests.
- CHECK YOUR WORK


## Tasks

```py
#settings.py

from datetime import timedelta
from pathlib import Path
import os
from configurations import Configuration, values

class Dev(Configuration):
    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = "django-insecure-p5+$5*@#^f3t#1274_h^ro0jnjtfpncj^(mikp#9&eh^u^v4lw"

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = ["localhost", "0.0.0.0", ".codio.io", os.environ.get('CODIO_HOSTNAME') + '-8000.codio.io']
    X_FRAME_OPTIONS = 'ALLOW-FROM ' + os.environ.get('CODIO_HOSTNAME') + '-8000.codio.io'
    CSRF_COOKIE_SAMESITE = None
    CSRF_TRUSTED_ORIGINS = [os.environ.get('CODIO_HOSTNAME') + '-8000.codio.io']
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SAMESITE = 'None'
    SESSION_COOKIE_SAMESITE = 'None'

    # Application definition

    INSTALLED_APPS = [
        "movienight_auth",
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "django_registration",
        "crispy_forms",
        "crispy_bootstrap5",
        "movies",
        "rest_framework",
        "rest_framework.authtoken",
    ]

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        # "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        # "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    ROOT_URLCONF = "movienight.urls"

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [BASE_DIR / "templates"],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]

    WSGI_APPLICATION = "movienight.wsgi.application"

    # Database
    # https://docs.djangoproject.com/en/3.2/ref/settings/#databases

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

    # Password validation
    # https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
        },
    ]

    # Internationalization
    # https://docs.djangoproject.com/en/3.2/topics/i18n/

    LANGUAGE_CODE = "en-us"

    TIME_ZONE = values.Value("UTC")

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.2/howto/static-files/

    STATIC_URL = "/static/"

    # Default primary key field type
    # https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

    AUTH_USER_MODEL = "movienight_auth.User"

    CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
    CRISPY_TEMPLATE_PACK = "bootstrap5"

    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

    ACCOUNT_ACTIVATION_DAYS = 7

    BASE_URL = "http://localhost:8000/"

    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose": {
                "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
                "style": "{",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "verbose",
            }
        },
        "root": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
    }

    OMDB_KEY = values.Value()

    SIMPLE_JWT = {
        "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
        "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    }
```

```py
# serializers.py

from rest_framework import serializers

from movienight_auth.models import User
from movies.models import Movie, MovieNight, MovieNightInvitation, Genre


class GenreField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        try:
            return self.get_queryset().get_or_create(name=data)[0]
        except (TypeError, ValueError):
            self.fail(f"Tag value {data} is invalid")


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreField(slug_field="name", many=True, read_only=True)

    class Meta:
        pass

class MovieTitleAndUrlSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedRelatedField("movie-detail", read_only=True)

    class Meta:
        model = Movie
        fields = ["title", "url"]


class MovieNightInvitationSerializer(serializers.ModelSerializer):
    invitee = serializers.HyperlinkedRelatedField(
        "user-detail", read_only=True, lookup_field="email"
    )

    class Meta:
        model = MovieNightInvitation
        fields = "__all__"
        read_only_fields = ["attendance_confirmed", "movie_night", "invitee"]


class MovieNightInvitationCreationSerializer(serializers.ModelSerializer):
    invitee = serializers.HyperlinkedRelatedField(
        "user-detail", queryset=User.objects.all(), lookup_field="email"
    )

    class Meta:
        model = MovieNightInvitation
        fields = ["invitee"]

    def __init__(self, movie_night, *args, **kwargs):
        self.movie_night = movie_night
        super(MovieNightInvitationCreationSerializer, self).__init__(*args, **kwargs)

    def save(self, **kwargs):
        kwargs["movie_night"] = self.movie_night
        return super(MovieNightInvitationCreationSerializer, self).save(**kwargs)

    def validate_invitee(self, invitee):
        existing_invitation = MovieNightInvitation.objects.filter(
            invitee=invitee, movie_night=self.movie_night
        ).first()
        if existing_invitation:
            raise serializers.ValidationError(
                f"{invitee.email} has already been invited to this Movie Night"
            )
        return invitee


class MovieNightSerializer(serializers.ModelSerializer):
    movie = MovieTitleAndUrlSerializer(read_only=True)
    creator = serializers.HyperlinkedRelatedField(
        "user-detail", read_only=True, lookup_field="email"
    )
    invites = MovieNightInvitationSerializer(read_only=True, many=True)

    class Meta:
        model = MovieNight
        fields = "__all__"
        read_only_fields = ["movie", "creator", "start_notification_sent", "invites"]


class MovieNightCreateSerializer(MovieNightSerializer):
    movie = serializers.HyperlinkedRelatedField(
        view_name="movie-detail", queryset=Movie.objects.all()
    )

    class Meta(MovieNightSerializer.Meta):
        read_only_fields = ["start_notification_sent", "invites"]


class MovieSearchSerializer(serializers.Serializer):
    term = serializers.CharField()

```

```py
# views.py

from django.shortcuts import redirect
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from movies.api.serializers import (
    MovieSerializer,
    MovieNightSerializer,
    MovieNightInvitationSerializer,
    GenreSerializer,
    MovieSearchSerializer,
    MovieNightInvitationCreationSerializer,
    MovieNightCreateSerializer,
)
from movies.models import Movie, MovieNight, MovieNightInvitation, Genre
from movies.omdb_integration import fill_movie_details, search_and_save


class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(methods=["get"], detail=False)
    def search(self, request):
        search_serializer = MovieSearchSerializer(data=request.GET)

        if not search_serializer.is_valid():
            return Response(search_serializer.errors)

        term = search_serializer.data["term"]

        search_and_save(term)

        movies = self.get_queryset().filter(title__icontains=term)

        page = self.paginate_queryset(movies)

        if page is not None:
            serializer = MovieSerializer(page, many=True, context={"request": request})
            return self.get_paginated_response(serializer.data)

        return Response(
            MovieSerializer(movies, many=True, context={"request": request}).data
        )


class MovieNightViewSet(viewsets.ModelViewSet):
    queryset = MovieNight.objects.all()

    def get_object(self):
        movie_night = super(MovieNightViewSet, self).get_object()
        if (
            movie_night.creator != self.request.user
            and movie_night.invites.filter(invitee=self.request.user).count() == 0
        ):
            raise PermissionDenied()
        return movie_night

    def get_queryset(self):
        if self.action == "list":
            return self.queryset.filter(creator=self.request.user)
        return super(MovieNightViewSet, self).get_queryset()

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    @action(detail=False)
    def invited(self, request):
        movie_nights = MovieNight.objects.filter(
            invites__in=MovieNightInvitation.objects.filter(invitee=request.user)
        )

        page = self.paginate_queryset(movie_nights)

        if page is not None:
            serializer = MovieNightSerializer(
                page, many=True, context={"request": request}
            )
            return self.get_paginated_response(serializer.data)

        return Response(
            MovieNightSerializer(
                movie_nights, many=True, context={"request": request}
            ).data
        )

    @action(methods=["post"], detail=True)
    def invite(self, request, pk):
        movie_night = self.get_object()
        if movie_night.creator != self.request.user:
            raise PermissionDenied()

        serializer = MovieNightInvitationCreationSerializer(
            movie_night, data=request.data, context={"request": request}
        )

        if not serializer.is_valid():
            return Response(serializer.errors)

        serializer.save()
        return redirect("movienight-detail", (movie_night.pk,))


class MovieNightInvitationViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = MovieNightInvitationSerializer

    def get_queryset(self):
        return MovieNightInvitation.objects.filter(invitee=self.request.user)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
```


## Solution

```py
# settings.py

    # existing code omitted

    REST_FRAMEWORK = {
        "DEFAULT_PERMISSION_CLASSES": [
            "rest_framework.permissions.IsAuthenticated",
        ],
        "DEFAULT_AUTHENTICATION_CLASSES": [
            "rest_framework.authentication.BasicAuthentication",
            "rest_framework.authentication.SessionAuthentication",
            "rest_framework.authentication.TokenAuthentication",
            "rest_framework_simplejwt.authentication.JWTAuthentication",
        ],
        "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
        "PAGE_SIZE": 100,
    }
```
- Add the REST_FRAMEWORK dictionary.
- Add IsAuthenticated to the list of default permission classes.
- Add basic, session, token, and JWT authentication to the default authentication classes.
- Use page number pagination for the default pagination class.
- Set the page size to 100.


```py
# views.py
# existing code omitted

class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_object(self):
        movie = super().get_object()
        fill_movie_details(movie)
        return movie

# existing code omitted

class MovieNightViewSet(viewsets.ModelViewSet):
    queryset = MovieNight.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST" or self.action == "create":
            return MovieNightCreateSerializer

        return MovieNightSerializer

# existing code omitted
```
- Add the get_object method to MovieViewSet. This method should call fill_movie_details.
- Implement the get_serializer_class method on MovieNightViewSet. If the action is "create" or "POST" then return the MovieNightCreate serializer. Otherwise return the MovieNightSerializer serializer.

```py
# serializer.py

# existing code omitted

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreField(slug_field="name", many=True, read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"
        read_only_fields = [
            "title",
            "year",
            "runtime_minutes",
            "imdb_id",
            "genres",
            "plot",
            "is_full_record",
        ]

# existing code omitted
```
- Add the model, fields and read_only_fields as attributes to the Meta class on MovieSerializer.