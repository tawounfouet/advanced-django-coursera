from django.test import TestCase
from django.conf import settings


class Question2TestCase(TestCase):
    def test_allowed_hosts_from_env(self):
        allowed_hosts = settings.ALLOWED_HOSTS
        self.assertIn(len(allowed_hosts), (2, 3))
        if len(allowed_hosts) == 3:
            self.assertIn("testserver", allowed_hosts)
        self.assertIn("host1.example.com", allowed_hosts)
        self.assertIn("host2.example.org", allowed_hosts)
