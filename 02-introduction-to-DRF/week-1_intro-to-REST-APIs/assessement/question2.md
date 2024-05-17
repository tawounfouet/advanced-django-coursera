# Introduction to REST APIs: Question 2

## Question 2
Similarly to Question 1, now “wire-up” the fruit_detail method to call handle_detail_get, handle_detail_put and handle_detail_delete, based on the request HTTP method. Pass the pk to each one, as well as request.body to handle_detail_put. Return an HttpResponseNotAllowed if an unsupported HTTP method is used.

## Solution GPT

```python
def fruit_detail(request, pk):
    # Question 2: Complete this function body
    if request.method == "GET":
        return handle_detail_get(pk)

    if request.method == "PUT":
        return handle_detail_put(pk, request.body)

    if request.method == "DELETE":
        return handle_detail_delete(pk)

    return HttpResponseNotAllowed(["GET", "PUT", "DELETE"])
```

## Solution - Codio 
```python
def fruit_detail(request, pk):
    # Question 2: Complete this function body
    if request.method == "GET":
        return handle_detail_get(pk)

    if request.method == "PUT":
        return handle_detail_put(pk, request.body)

    if request.method == "DELETE":
        return handle_detail_delete(pk)

    return HttpResponseNotAllowed(["GET", "PUT", "DELETE"])
```

- No additional modules need to be imported
- If the request method is GET, return the handle_detail_get method; pass it pk
- If the request method is PUT, return the handle_detail_putt method; pass it pk and request.body
- If the request method is DELETE, return the handle_detail_delete method; pass it pk
- Return the HttpResponseNotAllowed method if the request method is not GET, PUT, or DELETE