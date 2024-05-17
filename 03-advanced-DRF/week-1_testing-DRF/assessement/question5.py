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