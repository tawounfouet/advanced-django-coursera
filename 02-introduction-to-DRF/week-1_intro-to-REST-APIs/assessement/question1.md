# Introduction to REST APIs: Question 1

## Question 1
In assessment/views.py the view fruit_list has been created, and the URL /api/fruit/ points to it. There are also some empty functions, handle_list_get and handle_list_post. For this question, you need to call the correct function from the fruit_list view, based on the request method. However, you don’t yet need to implement these other functions. Pass the request.body to the handle_list_post function.
If an unsupported HTTP method is used then return an HttpResponseNotAllowed – make sure this includes the methods that are allowed.

## Task
```python
# Multiple Questions: Add imports here


def fruit_list(request):
    # Question 1: Complete this function body
    pass


def fruit_detail(request, pk):
    # Question 2: Complete this function body
    pass


def handle_list_get():
    # Question 3: Complete this function body
    pass


def handle_detail_get(pk):
    # Question 3: Complete this function body
    pass


def handle_list_post(body):
    # Question 4: Complete this function body
    pass


def handle_detail_put(pk, body):
    # Question 5: Complete this function body
    pass


def handle_detail_delete(pk):
    # Question 5: Complete this function body
    pass
```

## Solution

```python
# Multiple Questions: Add imports here
from django.http import HttpResponseNotAllowed

def fruit_list(request):
    # Question 1: Complete this function body
    if request.method == 'GET':
        return handle_list_get()
    elif request.method == 'POST':
        return handle_list_post(request.body)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])
```


## Provided Solution
```python
from django.http import HttpResponseNotAllowed

def fruit_list(request):
    # Question 1: Complete this function body
    if request.method == "GET":
        return handle_list_get()

    if request.method == "POST":
        return handle_list_post(request.body)

    return HttpResponseNotAllowed(["GET", "POST"])
```

- Import HttpResponseNotAllowed from django.http
- If the request method is GET, return the handle_list_get() method
- If the request method is POST, return the handle_list_post() method
- Return HttpResponseNotAllowed if the request method is not GET or POST