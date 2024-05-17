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