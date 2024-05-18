# Task Queuing: Intro
## Intro

In these questions you will be working with the project module2 which has one app, books. It is similar to the module1 project however does not fetch data from an "API".

The Author module has one extra field compared to the module1 version: book_count, which stores a count of all the Books by the author. This field must be updated manually and we will use signals and Celery to update it.

As with module1 the tests can all be run using python manage.py test or run individually by their test number, for example: python manage.py test books.tests_1.
