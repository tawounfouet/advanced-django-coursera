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