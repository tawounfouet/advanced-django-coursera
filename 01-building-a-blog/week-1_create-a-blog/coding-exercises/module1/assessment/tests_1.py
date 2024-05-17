from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase

from assessment.models import Thing, Comment


class Question1TestCase(TestCase):
    def setUp(self):
        self.user1 = get_user_model().objects.create(
            username="test_user1", password="MySuperSecurePassword1!@#$"
        )

    def test_commenting_on_thing(self):
        t = Thing.objects.create(owner=self.user1)
        c1 = Comment.objects.create(content="This is a great thing!", content_object=t)
        c2 = Comment.objects.create(content="This is so terrible!", content_object=t)

        t_comments = t.comments.all()

        self.assertIn(c1, t_comments)
        self.assertIn(c2, t_comments)
        self.assertEqual(len(t_comments), 2)

        self.assertEqual(c1.content_type, ContentType.objects.get_for_model(Thing))
        self.assertEqual(c1.object_id, t.pk)
        self.assertEqual(c1.content_object, t)

        self.assertEqual(c2.content_type, ContentType.objects.get_for_model(Thing))
        self.assertEqual(c2.object_id, t.pk)
        self.assertEqual(c2.content_object, t)
