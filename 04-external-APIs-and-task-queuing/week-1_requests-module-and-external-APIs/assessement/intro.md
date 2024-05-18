# Requests Module and External APIs: Intro

## Intro
In these questions you will be setting up API access using similar methods to what was discussed for accessing the OMDb API. We’ll use a fake service for retrieving book information, that’s accessed with a mock client. The service is called MyBookStore. The data is hard-coded on the MyBookStoreClient class, in its data attribute. You can pretend that MyBookStoreClient.data is the equivalent of the JSON-decoded data from a REST API.

The project is called module1 and has one app, books. There are two models already created. Book and Author. They are quite simple and self-explanatory. The Django admin has been set up for these models but you should be able to complete these questions just by running the unit tests.

As usual, they can all be run using python manage.py test or run individually by their test number, for example: python manage.py test books.tests_1.
