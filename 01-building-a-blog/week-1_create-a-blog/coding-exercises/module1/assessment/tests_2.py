from html.parser import HTMLParser

from django.test import TestCase


class RowColumnParser(HTMLParser):
    in_container = False
    in_row = False
    in_column = False

    def __init__(self):
        self.rows = []

        super(RowColumnParser, self).__init__()

    def handle_starttag(self, tag, attrs):
        if tag != "div":
            return

        attrs = dict(attrs)

        if attrs.get("id") == "question-2-container":
            self.in_container = True
            return

        if not self.in_container:
            return

        if attrs.get("class") == "row":
            self.rows.append([])
            self.in_row = True
            return

        if not self.in_row:
            return

        if "col" in attrs.get("class", ""):
            self.in_column = True
            self.rows[-1].append(
                set(filter(lambda c: c.startswith("col"), attrs["class"].split()))
            )

    def handle_endtag(self, tag):
        if tag != "div":
            return

        if self.in_column:
            self.in_column = False
            return

        if self.in_row:
            self.in_row = False
            return

        if self.in_container:
            self.in_container = False
            return

    def error(self, message):
        raise ValueError(message)


class Question2TestCase(TestCase):
    def setUp(self):
        resp = self.client.get("/question2/")
        self.parser = RowColumnParser()
        self.parser.feed(resp.content.decode("utf8"))

    def test_first_row(self):
        self.assertEqual(len(self.parser.rows), 2)
        self.assertEqual(len(self.parser.rows[0]), 2)

        col1_classes = self.parser.rows[0][0]
        col2_classes = self.parser.rows[0][1]

        self.assertEqual(len(col1_classes), 2)
        self.assertEqual(len(col2_classes), 2)

        self.assertIn("col-md-6", col1_classes)
        self.assertTrue("col-12" in col1_classes or "col-xs-12" in col1_classes)

        self.assertIn("col-md-6", col2_classes)
        self.assertTrue("col-12" in col2_classes or "col-xs-12" in col2_classes)

    def test_second_row(self):
        self.assertEqual(len(self.parser.rows), 2)
        self.assertEqual(len(self.parser.rows[1]), 3)

        col1_classes = self.parser.rows[1][0]
        col2_classes = self.parser.rows[1][1]
        col3_classes = self.parser.rows[1][2]

        self.assertEqual(len(col1_classes), 2)
        self.assertEqual(len(col2_classes), 2)
        self.assertEqual(len(col3_classes), 2)

        self.assertIn("col-md-3", col1_classes)
        self.assertTrue("col-6" in col1_classes or "col-xs-6" in col1_classes)

        self.assertIn("col-md-3", col2_classes)
        self.assertTrue("col-6" in col2_classes or "col-xs-6" in col2_classes)

        self.assertIn("col-md-6", col3_classes)
        self.assertTrue("col-12" in col3_classes or "col-xs-12" in col3_classes)
