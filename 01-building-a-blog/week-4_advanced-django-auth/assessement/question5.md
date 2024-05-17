# Advanced Django Authentication: Question 5

## Question 5
Carrying on from Question 4, set up the URL mappings to the Django Registration views, we will use the one_step method. Then, you’ll need to render the registration form in the registration_form.html template, where indicated. Using the crispy template tag can make this easy.
You can test this works by registering a user at /accounts/register/.


## Problem
```html
{% extends "base.html" %}
{% load crispy_forms_tags %}
{% block title %}Question 5{% endblock %}
{% block content %}
    {# Question 5: Render the registration form #}
{% endblock %}
```

```python
"""module4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # Question 3 & 5: Add imports
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/profile/", TemplateView.as_view(template_name="profile.html")),
    # Question 3 & 5: Set up URL maps here
    path("accounts/", include("django.contrib.auth.urls")),  # Include the Django auth URLs
]

```


## Solution - not correct

```python
"""module4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django_registration.backends.one_step.views import RegistrationView
from assessment.forms import CustomRegistrationForm

# Question 3 & 5: Add imports
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/profile/", TemplateView.as_view(template_name="profile.html")),
    # Question 3 & 5: Set up URL maps here
    path("accounts/register/", 
         RegistrationView.as_view(form_class=CustomRegistrationForm), 
         name="django_registration_register"),
    path("accounts/", include("django_registration.backends.one_step.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]

```



## Solution - Correct 
```python
from django.contrib import admin
from django.urls import path, include

# Question 3 & 5: Add imports
from django.views.generic import TemplateView
from django_registration.backends.one_step.views import RegistrationView

from assessment.forms import CustomRegistrationForm

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/profile/", TemplateView.as_view(template_name="profile.html")),
    # Question 3 & 5: Set up URL maps here
    path("accounts/", include("django.contrib.auth.urls")),
    path(
        "accounts/register/",
        RegistrationView.as_view(form_class=CustomRegistrationForm),
        name="django_registration_register",
    ),
    path("accounts/", include("django_registration.backends.one_step.urls")),
]
```


```html
{% extends "base.html" %}
{% load crispy_forms_tags %}
{% block title %}Question 4{% endblock %}
{% block content %}
    {# Question 5: Render the registration form #}
    {% crispy form %}
{% endblock %}
```