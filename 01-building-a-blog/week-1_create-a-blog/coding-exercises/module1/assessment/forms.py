# Question 5: Add your imports here
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from assessment.models import Thing


class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ["name"]

    def __init__(self, *args, **kwargs):
        super(ThingForm, self).__init__(*args, **kwargs)
        # Question 5: Implement Crispy Form Setup below
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))