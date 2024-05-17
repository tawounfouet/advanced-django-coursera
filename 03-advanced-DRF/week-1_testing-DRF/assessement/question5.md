# Testing Django Rest Framework: Question 5

## Question 5
For the final test case Question5TestCase (in the assessment/questions/question_4.py file), we once again want to use a live server and RequestsClient. Add the imports that you need and update the class definition. Then, update the setUp() method to create a test user and fetch a token (use the /api/v1/token-auth/ endpoint to request the token). Set the token into the correct header on the client so it will be used in the test method. You do not need to make any changes to the test_post_create() method.

Note that for the assessment to pass you must import RequestsClient in a particular way, so we have already imported it for you in this question file.

## Login Information
In order for all of your tests to pass, use test as the username and password as the password.
Write your test and run it in the terminal before submitting your code for evaluation.

## Run Your Test
Enter the command below in the terminal to run your test:
python3 manage.py test_assessment 5

## Check Your Test
Enter the command below in the terminal to check your test before submitting your code:
python3 manage.py test assessment.tests_5


## Task
```python
# Question 4: Add your imports here

from rest_framework.test import RequestsClient

from assessment.models import Post

# Question 5: Set up inheritance here
class Question5TestCase:
    """
    This TestCase can be executed with the command:
    python3 manage.py test_assessment 5
    """

    def setUp(self):
        # Question 5: Set up the user and client here
        pass

    def test_post_create(self):
        # Do not change this method
        self.client.post(
            self.live_server_url + "/api/v1/posts/",
            {"title": "Post 1", "content": "Post 1 Content", "slug": "post-1"},
        )

        post = Post.objects.first()

        self.assertEqual(post.title, "Post 1")
        self.assertEqual(post.content, "Post 1 Content")
        self.assertEqual(post.slug, "post-1")
```

## Solution

```python
from django.contrib.auth import get_user_model
from django.test import LiveServerTestCase
from rest_framework.test import RequestsClient

from assessment.models import Post


class Question5TestCase(LiveServerTestCase):
    """
    This TestCase can be executed with the command:
    python3 manage.py test_assessment 5
    """

    def setUp(self):
        # Question 5: Set up the user and client here
        get_user_model().objects.create_user(username="test", password="password")
        self.client = RequestsClient()
        token_resp = self.client.post(
            self.live_server_url + "/api/v1/token-auth/",
            {"username": "test", "password": "password"},
        )
        self.client.headers["Authorization"] = "Token " + token_resp.json()["token"]

    def test_post_create(self):
        # Do not change this method
        self.client.post(
            self.live_server_url + "/api/v1/posts/",
            {"title": "Post 1", "content": "Post 1 Content", "slug": "post-1"},
        )

        post = Post.objects.first()

        self.assertEqual(post.title, "Post 1")
        self.assertEqual(post.content, "Post 1 Content")
        self.assertEqual(post.slug, "post-1")

```