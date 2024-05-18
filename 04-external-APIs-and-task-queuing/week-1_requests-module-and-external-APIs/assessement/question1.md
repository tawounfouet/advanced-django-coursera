# Question 1
To “access” our “API” we need an API key of ABC123. The MyBookStoreClient class (my_book_store.client.MyBookStoreClient) must be instantiated with the API key as the argument to its constructor. To make it easier to instantiate a my_book_store/django_client.py, you should implement the helper function get_client_from_settings() in my_book_store/django_client.py. It should instantiate and return a MyBookStoreClient instance, using the MBS_API_KEY setting; you’ll need to add this to settings.py too.

## Task
```python
# Question 1: Add any imports you need


def get_client_from_settings():
    # Question 1: implement this function
    pass
```

## Solution
```python
# Question 1: Add any imports you need
from django.conf import settings

from my_book_store.client import MyBookStoreClient


def get_client_from_settings():
    # Question 1: implement this function
    return MyBookStoreClient(settings.MBS_API_KEY)
```
- Import settings and MyBookStoreClient
- Return an instance of MyBookStoreClient with MBS_API_KEY as the paramete


```python
# settings.py

# Question 1: Add your setting here
MBS_API_KEY = "ABC123"
```

- Set a value for MBS_API_KEY to "ABC123".