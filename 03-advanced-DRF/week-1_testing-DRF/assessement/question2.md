# Testing Django Rest Framework: Question 2

## Question 2
As well as making use of APIClient on Question2TestCase (in the assessment/questions/question_2.py file) we want to create a test user and authenticate the client. Remember that in this project we’re using the default Django User model, so it should be created with a username and password (not email and password). Add the imports and update the setUp() method to make this change. Use the login() method to authenticate the client.

## Login Information
In order for all of your tests to pass, use test as the username and password as the password.

Write your test and run it in the terminal before submitting your code for evaluation.

## Run Your Test
Enter the command below in the terminal to run your test:
python3 manage.py test_assessment 2

## Check Your Test
Enter the command below in the terminal to check your test before submitting your code:
python3 manage.py test assessment.tests_2


## Task
```python
# Question 2: Add your imports here
from django.test import TestCase

from assessment.models import Post


class Question2TestCase(TestCase):
    """
    This TestCase can be executed with the command:
    python3 manage.py test_assessment 2
    """

    def setUp(self):
        # Question 2: Perform the necessary setup for the user and client here
        pass

    def test_post_create(self):
        # Do not change this method
        resp = self.client.post(
            "/api/v1/posts/",
            {"title": "Post 1", "content": "Post 1 Content", "slug": "post-1"},
        )
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(Post.objects.count(), 1)

    def test_post_create_unauthenticated(self):
        # Do not change this method
        self.client.logout()
        resp = self.client.post(
            "/api/v1/posts/",
            {"title": "Post 1", "content": "Post 1 Content", "slug": "post-1"},
        )
        self.assertEqual(resp.status_code, 401)
        self.assertEqual(Post.objects.count(), 0)
```

## Solution
```python
# Question 2: Add your imports here
from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

from assessment.models import Post


class Question2TestCase(TestCase):
    """
    This TestCase can be executed with the command:
    python3 manage.py test_assessment 2
    """

    def setUp(self):
        # Question 2: Perform the necessary setup for the user and client here
        self.u1 = get_user_model().objects.create_user(
            username="test", password="password"
        )
        self.client = APIClient()
        self.client.login(username="test", password="password")

    def test_post_create(self):
        # Do not change this method
        resp = self.client.post(
            "/api/v1/posts/",
            {"title": "Post 1", "content": "Post 1 Content", "slug": "post-1"},
        )
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(Post.objects.count(), 1)

    def test_post_create_unauthenticated(self):
        # Do not change this method
        self.client.logout()
        resp = self.client.post(
            "/api/v1/posts/",
            {"title": "Post 1", "content": "Post 1 Content", "slug": "post-1"},
        )
        self.assertEqual(resp.status_code, 401)
        self.assertEqual(Post.objects.count(), 0)
```

- Import get_user_model and APIClient
- Create a test user with the username test and password password
- Use APIClient for testing
- Login with the test user