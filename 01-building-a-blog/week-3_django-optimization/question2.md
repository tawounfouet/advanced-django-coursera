# Question 2
The view question2 has been set up with the URL /question2/. It returns the current time, but also the username of the logged in users (or AnonymousUser if no user is logged in). Cache the response for 120 seconds, but remember, different users should get different responses.

## Testing Your Code
- Refresh the page several times. The time should not change.
- Wait two minutes, then refresh again. The time should update since it is no longer cached.
- If you are not logged in, you should see AnonymousUser on the screen.
- Go to the /admin page (replace /question2 with /admin) and log in with admin and secrets!.
- Return to the /question2 (replace /admin with /question2) page, you should see admin on the screen.

## Problem

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


## Solution

```python
import datetime

from django.http import HttpResponse
from django.shortcuts import render
from assessment.models import get_test_resources, Resource

# Question 1 & 2: Add your imports here
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

# Question 2: Cache this view, make sure it's different for each user
@cache_page(120)
@vary_on_cookie
def question2(request):
    # Do not change this function body
    return HttpResponse(datetime.datetime.now().isoformat() + str(request.user))
```

- Import vary_on_cookie from django.views.decorators.vary
- Add the a decorator to cache the page for 120 seconds
- Add a decorator so the output varies on cookies