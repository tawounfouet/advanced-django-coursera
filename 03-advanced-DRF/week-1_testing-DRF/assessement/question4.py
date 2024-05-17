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