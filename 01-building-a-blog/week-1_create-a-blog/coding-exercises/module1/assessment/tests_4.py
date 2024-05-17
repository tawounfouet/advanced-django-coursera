from django.test import TestCase


class Question4TestCase(TestCase):
    def test_comments_for_thing_tag(self):
        resp = self.client.get("/question4/")

        self.assertIn(
            b"<li>A cardigan is the best type of clothing.</li>", resp.content
        )
        self.assertIn(b"<li>I agree, it&#x27;s great.</li>", resp.content)
        self.assertIn(
            b"<li>Not sure about these statements.</li>",
            resp.content,
        )
