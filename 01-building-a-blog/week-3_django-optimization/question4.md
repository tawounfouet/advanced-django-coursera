# Question 4
The project contains a simple model, Resource, which has two attributes, name and cost. The function get_test_resources() deletes all existing Resource objects, then returns three new Resource objects. These new objects will only be saved to the database if the save_to_db argument is set to True.

The view question4 (which the URL /question4/ points to) has been set up to call the get_test_resources() function, then do another query which returns a description of all the test Resource objects in the database.

You need to update the question4 function to perform a bulk create of all the test_resources objects at once.

## Testing Your Code
Start the dev server and open the site.

You should see the following output on the screen:

```sh
Pk: 1 Name: Res 1 Cost: 1 Pk: 2 Name: Res 2 Cost: 2 Pk: 3 Name: Res 3 Cost: 3 
```

## Problem
```python
import datetime

from django.http import HttpResponse
from django.shortcuts import render

from assessment.models import get_test_resources, Resource

# Question 1 & 2: Add your imports here
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

# Question 1: Cache this view
@cache_page(120)
def question1(request):
    # Do not change this function body
    return HttpResponse(datetime.datetime.now().isoformat())


# Question 2: Cache this view, make sure it's different for each user
@cache_page(120)
@vary_on_cookie
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

## Solution

```python
def question4(request):
    test_resources = get_test_resources()

    # Question 4: Add code to insert all test resources at once below
    Resource.objects.bulk_create(test_resources)

    return HttpResponse(", ".join(map(str, Resource.objects.all())))
```

- Use the bulk_create method to do all the updates at once.
- Pass it the test_resources variable as an argument.