from configurations import Configuration
from configurations.values import SecretValue
from django.test import TestCase
from module2.settings import Dev, Prod


class Question3TestCase(TestCase):
    def test_prod_class_set_up(self):
        self.assertTrue(issubclass(Dev, Configuration))
        self.assertTrue(issubclass(Prod, Dev))

    def test_debug_values(self):
        self.assertTrue(Dev.DEBUG)
        self.assertFalse(Prod.DEBUG)

    def test_secret_value(self):
        self.assertIsInstance(Dev.SECRET_KEY, str)
        self.assertIsInstance(Prod.SECRET_KEY, SecretValue)
