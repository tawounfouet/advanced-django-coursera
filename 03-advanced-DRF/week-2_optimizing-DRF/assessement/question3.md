# Optimizing Django Rest Framework: Question 3

## Question 3
Add throttling for logged-in users as well, but with a limit of 100 requests per minute.

```python
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly"
    ],
    # Questions 2 & 3: Make changes to this setting
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {"anon": "10/min", "user": "100/min"},
}
```
- Add user throttling to DEFAULT_THROTTLE_CLASS
- Set the throttle rate for logged-in users at 100 per minute