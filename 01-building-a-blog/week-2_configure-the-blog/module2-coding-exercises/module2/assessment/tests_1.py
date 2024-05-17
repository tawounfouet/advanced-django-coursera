from configurations import Configuration
from django.test import TestCase
from module2 import settings


class Question1TestCase(TestCase):
    def test_dev_class_set_up(self):
        self.assertTrue(issubclass(settings.Dev, Configuration))
        self.assertTrue(settings.Dev.DEBUG)
        self.assertIsInstance(settings.Dev.INSTALLED_APPS, list)
