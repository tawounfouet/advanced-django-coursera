# Question 5
A ThingForm has been created in assessment/forms.py. It needs to be made “crispy” to work with Django Crispy Forms. That is, add a FormHelper and a submit button to the class. You can do this by adding code to the __init__ method and importing the classes you need


### Problem

```python
# Question 5: Add your imports here
from django import forms


from assessment.models import Thing


class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ["name"]

    def __init__(self, *args, **kwargs):
        super(ThingForm, self).__init__(*args, **kwargs)
        # Question 5: Implement Crispy Form Setup below

```

### Solution

```python
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
```

- Import FormHelper from crispy_forms.helper
- Import Submit from crispy_forms.layout
- Instantiate a FormHelper object and call it self.helper
- Instantiate and add a Submit object to self.helper




```python
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
        self.helper = FormHelper()
        self.helper.form_method = 'post'  # Specify the form method (post)
        self.helper.add_input(Submit('submit', 'Save'))  # Add a submit button with the label 'Save'
```