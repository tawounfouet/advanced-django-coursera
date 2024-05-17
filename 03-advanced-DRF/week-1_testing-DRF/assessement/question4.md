# Testing Django Rest Framework: Question 4

## Question 4
For the Question4TestCase (in the assessment/questions/question_4.py file), we would like this test case to use the live test server for the tests, and the RequestsClient to make requests. You’ll need to add some imports and change the class definition, then set the client in the setUp() method. After you’ve done this, implement the test_post_list method. It should use the client set in setUp() to request the list of Post object, making sure you use the right live server URL. Then the only test that is required is to check that the length of the returned data is 2. Use the assertEqual() assertion to test this.
Write your test and run it in the terminal before submitting your code for evaluation.

## Run Your Test
Enter the command below in the terminal to run your test:
python3 manage.py test_assessment 4

## Check Your Test
Enter the command below in the terminal to check your test before submitting your code:
python3 manage.py test assessment.tests_4

## Task

```python
# Question 4: Add your imports here

from assessment.models import Post


# Question 4: Update the class definition
class Question4TestCase:
    """
    This TestCase can be executed with the command:
    python3 manage.py test_assessment 4
    """

    def setUp(self):
        Post.objects.create(title="Post 1", content="Post 1 Content", slug="post-1")
        Post.objects.create(title="Post 2", content="Post 2 Content", slug="post-2")
        # Question 4: Set up the client here

    def test_post_list(self):
        # Question 4: Request the Post list and check that it has a length of 2
        
```

## Solution
```python
# Question 4: Add your imports here
from django.test import LiveServerTestCase
from rest_framework.test import RequestsClient

from assessment.models import Post


# Question 4: Update the class definition
class Question4TestCase(LiveServerTestCase):
    """
    This TestCase can be executed with the command:
    python3 manage.py test_assessment 4
    """

    def setUp(self):
        Post.objects.create(title="Post 1", content="Post 1 Content", slug="post-1")
        Post.objects.create(title="Post 2", content="Post 2 Content", slug="post-2")
        # Question 4: Set up the client here
        self.client = RequestsClient()

    def test_post_list(self):
        # Question 4: Request the Post list and check that it has a length of 2
        resp = self.client.get(self.live_server_url + "/api/v1/posts/")
        self.assertEqual(len(resp.json()), 2)
```

- Import LiveServerTestCase and RequestsClient
- In setUp, set self.client to RequestsClient()
- In test_post_list set the response to the live server URL plus "/api/v1/posts/"
- Assert that the length of the response is 2