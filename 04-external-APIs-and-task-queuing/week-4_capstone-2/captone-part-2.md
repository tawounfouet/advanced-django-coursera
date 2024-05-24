# Capstone Part 2

## Movie Night Continued
In the final module of the final course, you will finish the Movie Night project you started in Module 3. This will involve making some changes to be a 12-Factor app, Django Rest Framework configuration, and Celery setup.

## REST API
The REST API URLs have been set up for you, you will mostly just be making a few minor changes to the viewsets and serializers.

Here is a list of URLs that have been configured:
- api/v1/auth/login: Standard DRF login and logout views
- api/v1/token-auth/: API view for obtaining a DRF token.
- api/v1/jwt/: For obtaining a JWT.
- api/v1/jwt/refresh/: For refreshing a JWT.
- api/v1/movienight-auth/users/<email>: Get information about a user by email.
- api/v1/movies/movies/<pk>: List Movies or get detail by PK. Note that this endpoint is read-only.
- api/v1/movies/movies/search/: Search for Movies, with a term argument provided in the query string. This will call search_and_save() on the term first, before querying the database.
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

With the exception of a couple of endpoints, the design of this REST API is similar to what you have seen before.

Now let’s move on to the final assessment for this course.
Next