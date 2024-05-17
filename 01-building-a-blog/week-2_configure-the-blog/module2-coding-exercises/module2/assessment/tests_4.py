from django.conf import settings
from django.test import TestCase


class Question4TestCase(TestCase):
    def test_handlers_configuration(self):
        expected_handlers = {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "verbose",
            },
        }

        self.assertEqual(settings.LOGGING["handlers"], expected_handlers)

    def test_root_configuration(self):
        expected_root = {
            "handlers": ["console"],
            "level": "DEBUG",
        }
        self.assertEqual(settings.LOGGING["root"], expected_root)
