from django_registration.forms import RegistrationForm

# Question 4: Add your imports here
from assessment.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CustomRegistrationForm(RegistrationForm):
    # Question 4: Complete the class body
    class Meta(RegistrationForm.Meta):
        model = User

    def __init__(self, *args, **kwargs):
        super(CustomRegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Register"))
