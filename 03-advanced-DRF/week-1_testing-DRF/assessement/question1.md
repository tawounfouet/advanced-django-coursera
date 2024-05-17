# Testing Django Rest Framework: Question 1

## Question 1
We wish to replace the built-in Django test client on the Question1TestCase class (in the assessment/questions/question_1.py file) with Django Rest Framework’s APIClient. Add the imports and update the setUp() method to make this change.

Write your test and run it in the terminal before submitting your code for evaluation.

## Run Your Test
Enter the command below in the terminal to run your test:
python3 manage.py test_assessment 1

## Check Your Test
Enter the command below in the terminal to check your test before submitting your code:
python3 manage.py test assessment.tests_1



## Task
```python
from django.test import TestCase

# Question 1: Add your imports here

from assessment.models import Post


class Question1TestCase(TestCase):
    """
    This TestCase can be executed with the command:
    python3 manage.py test_assessment 1
    """

    def setUp(self):
        # Question 1: Make changes to the setUp method to use the APIClient
        pass

    def test_post_list(self):
        # Do not change this method
        Post.objects.create(title="Post 1", content="Post 1 Content", slug="post-1")
        Post.objects.create(title="Post 2", content="Post 2 Content", slug="post-2")

        resp = self.client.get("/api/v1/posts/")
        self.assertEqual(len(resp.json()), 2)
```


## Solution
```python
from django.test import TestCase

# Question 1: Add your imports here
from rest_framework.test import APIClient

from assessment.models import Post


class Question1TestCase(TestCase):
    """
    This TestCase can be executed with the command:
    python3 manage.py test_assessment 1
    """

    def setUp(self):
        # Question 1: Make changes to the setUp method to use the APIClient
        self.client = APIClient()

    def test_post_list(self):
        # Do not change this method
        Post.objects.create(title="Post 1", content="Post 1 Content", slug="post-1")
        Post.objects.create(title="Post 2", content="Post 2 Content", slug="post-2")

        resp = self.client.get("/api/v1/posts/")
        self.assertEqual(len(resp.json()), 2)
```

- Import APIClient
- Set self.client to APIClient to override the default Django test client