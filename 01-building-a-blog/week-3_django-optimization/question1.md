# Django Optimization: Question 1

## Question 1

The view question1 has been set up with the URL /question1/. It returns the current time, or, the time at which the response was cached. In this first question you should cache the response from the view for 120 seconds.

## Testing Your Code
- Refresh the page several times. The time should not change.
- Wait two minutes, then refresh again. The time should update since it is no longer cached.


## Problem

```python
import datetime

from django.http import HttpResponse
from django.shortcuts import render

from assessment.models import get_test_resources, Resource

# Question 1 & 2: Add your imports here


# Question 1: Cache this view
def question1(request):
    # Do not change this function body
    return HttpResponse(datetime.datetime.now().isoformat())


# Question 2: Cache this view, make sure it's different for each user
def question2(request):
    # Do not change this function body
    return HttpResponse(datetime.datetime.now().isoformat() + str(request.user))


def question3(request):
    # Do not change this function body
    return render(request, "question3.html")


def question4(request):
    test_resources = get_test_resources()

    # Question 4: Add code to insert all test resources at once below

    return HttpResponse(", ".join(map(str, Resource.objects.all())))


def question5(request):
    test_resources = get_test_resources(save_to_db=True)

    # Question 5: Add code to update all test resources then save with a bulk call below

    return HttpResponse(", ".join(map(str, Resource.objects.all())))
```


## solution

```python
import datetime

from django.http import HttpResponse
from django.shortcuts import render

from assessment.models import get_test_resources, Resource

# Question 1 & 2: Add your imports here
from django.views.decorators.cache import cache_page

# Question 1: Cache this view
@cache_page(120)
def question1(request):
    # Do not change this function body
    return HttpResponse(datetime.datetime.now().isoformat())
```

- Import cache_page from django.views.decorators.cache
- Add the cache_page decorator to the question1 function
- Pass 120 to the decorator so the information is cached for two minutes