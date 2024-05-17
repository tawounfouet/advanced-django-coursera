# Advanced Django Authentication: Question 4

## Question 4
We’ll now set up Django Registration to allow users to sign up through the site. The first step is to set up a form for registration. The class CustomRegistrationForm has been created in assessment/forms.py but its body needs to be completed. Set up the Meta attributes to use the custom User model. Then, write an __init__ method to add the Crispy form helper with a submit button with the text Register.

## Problem
```python
from django_registration.forms import RegistrationForm

# Question 4: Add your imports here


class CustomRegistrationForm(RegistrationForm):
    # Question 4: Complete the class body
    pass

```

## Solution - not good

```python
from django_registration.forms import RegistrationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# Question 4: Add your imports here
from assessment.models import User


class CustomRegistrationForm(RegistrationForm):
    # Question 4: Complete the class body
    
    class Meta(RegistrationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('register', 'Register'))
```

## Solution - Correct

```python
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
```

- Import User from assessments.models
- Import Submit and FormHelper from crispy_forms
- Create a Meta class
- In the constructor, add a Crispy form helper and a “Register” button