from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.test import TestCase
from .forms import ThingForm


class Question5TestCase(TestCase):
    def test_forms_helper(self):
        tf = ThingForm()

        self.assertTrue(hasattr(tf, "helper"))
        self.assertIsInstance(tf.helper, FormHelper)
        self.assertTrue(len(tf.helper.inputs), 1)
        submit_button = tf.helper.inputs[0]
        self.assertIsInstance(submit_button, Submit)
        self.assertEqual(submit_button.name, "submit")
        self.assertEqual(submit_button.value, "Submit")
