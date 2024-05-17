from django.test import TestCase


class Question3TestCase(TestCase):
    def test_full_name_filter(self):
        resp = self.client.get("/question3/")

        self.assertIn(b"User 1 Full Name: <em>Leo</em>, Lucio", resp.content)
        self.assertIn(b"User 2 Full Name: Lily", resp.content)
        self.assertIn(
            b"User 3 Full Name: <em>&lt;a href=&quot;bad-site&quot;&gt;Evil&lt;/a&gt;</em>, Hacker &gt; You",
            resp.content,
        )
