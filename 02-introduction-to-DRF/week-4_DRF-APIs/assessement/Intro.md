# Django Rest Framework APIs: Intro

## Intro
In this exercise we’re carrying on with the same Bakery API as we used in Module 3, so the models and URLs will be familiar. You will make some changes to implement the same API using viewsets and routers. You will mostly be editing the bakery/api/views.py file and module4/urls.py. Like in Module 3, the bakery/api/assessment_*.py files do not need to be edited.

You will need to run the manage.py migrate command to set up the database, and the create_fixtures command has been included to set up some test data for you. For simplicity no authentication is needed when working with this project.

Before submitting, you can run the tests for each question individually, e.g. python manage.py test bakery.tests_1