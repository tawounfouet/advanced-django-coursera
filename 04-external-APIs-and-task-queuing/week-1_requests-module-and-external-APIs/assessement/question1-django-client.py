# Question 1: Add any imports you need
from django.conf import settings

from my_book_store.client import MyBookStoreClient


def get_client_from_settings():
    # Question 1: implement this function
    return MyBookStoreClient(settings.MBS_API_KEY)