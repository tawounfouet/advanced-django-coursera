# Advanced Django Authentication: Question 3

## Question 3
Next we want to start using the Django authentication system so that users can log in. A template and URL have been set up for the profile page (/accounts/profile/), but that’s all that’s been done. You will need to first finish the template for the login form, which has already been created in assessment/templates/registration/login.html. Where indicated in the template add the <form> tags, and then render the login form (which is passed in the form context variable). You can use the crispy filter to make the form look a bit better, but not the crispy template tag.

Once you have done that, map the Django auth URLs in urls.py. You can create a user with the manage.py createsuperuser command and verify that it can log in.


## Problem

```html
{% extends "base.html" %}
{% load crispy_forms_tags %}
{% block title %}Question 2{% endblock %}
{% block content %}
    {# Question 3: Add the login form here #}
    
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
from django.urls import path

# Question 3 & 5: Add imports
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/profile/", TemplateView.as_view(template_name="profile.html")),
    # Question 3 & 5: Set up URL maps here
]
```


## Solution

```html
{# Question 3: Add the login form here #}
    <form method="post">
        {% csrf_token %}
        {{ form|crispy }}
        <button type="submit" class="btn btn-primary">Log In</button>
    </form>
```



```python
# Question 3 & 5: Add imports
from django.views.generic import TemplateView
from django.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/profile/", TemplateView.as_view(template_name="profile.html")),
    # Question 3 & 5: Set up URL maps here
    path("accounts/", include("django.contrib.auth.urls")),
]
```