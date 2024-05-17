# Question 5
The view question5 (which the URL /question5/ points to) is similar to question4, except get_test_resources() will save the objects in the database.

You need to add 10 to the cost of each Resource in test_resources and then make a single call to save all the Resource objects back to the database in bulk.

## Testing Your Code
You should see the following output on the screen:
```sh
Pk: 4 Name: Res 1 Cost: 11 Pk: 5 Name: Res 2 Cost: 12 Pk: 6 Name: Res 3 Cost: 13 
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
    Resource.objects.bulk_create(test_resources)

    return HttpResponse(", ".join(map(str, Resource.objects.all())))



def question5(request):
    test_resources = get_test_resources(save_to_db=True)

    # Question 5: Add code to update all test resources then save with a bulk call below

    return HttpResponse(", ".join(map(str, Resource.objects.all())))
```

## Solution

```python
def question5(request):
    # Retrieve test resources and save them to the database
    test_resources = get_test_resources(save_to_db=True)

    # Add 10 to the cost of each resource
    for resource in test_resources:
        resource.cost += 10

    # Perform a bulk update to save all modified resources
    Resource.objects.bulk_update(test_resources, ['cost'])

    return HttpResponse(", ".join(map(str, Resource.objects.all())))
```


```python

def question5(request):
    test_resources = get_test_resources(save_to_db=True)

    # Question 5: Add code to update all test resources then save with a bulk call below
    for r in test_resources:
        r.cost += 10

    Resource.objects.bulk_update(test_resources, ["cost"])

    return HttpResponse(", ".join(map(str, Resource.objects.all())))
```


- Iterate over test_resources
- Add 10 to the cost for each Resource
- Use bulk_update to update all of the Resource objects