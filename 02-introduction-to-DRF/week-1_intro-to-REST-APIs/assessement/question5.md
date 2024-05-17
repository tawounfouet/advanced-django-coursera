# Question 5
Implement Fruit updating by completing the handle_detail_put function. The body will be a JSON encoded dictionary which will contain some of the keys as the return value from fruit_to_dict. Assume that the body will not contain any invalid keys. Make sure to return a response with an appropriate status code.
Finally, implement the handle_detail_delete function, and return a response with an appropriate status code.
Make sure that both functions raise django.http.Http404 if a Fruit with the specified pk is not found.


## Solution - GPT
```python
def handle_detail_put(pk, body):
    try:
        fruit = Fruit.objects.get(pk=pk)
    except Fruit.DoesNotExist:
        raise Http404("Fruit not found")

    data = json.loads(body)
    for key, value in data.items():
        setattr(fruit, key, value)
    fruit.save()

    return HttpResponse(status=HTTPStatus.OK)



def handle_detail_delete(pk):
    try:
        fruit = Fruit.objects.get(pk=pk)
    except Fruit.DoesNotExist:
        raise Http404("Fruit not found")

    fruit.delete()
    return HttpResponse(status=HTTPStatus.NO_CONTENT)
```

## Solution - Codio
```python
from django.shortcuts import get_object_or_404

def handle_detail_put(pk, body):
    # Question 5: Complete this function body
    f = get_object_or_404(Fruit, pk=pk)
    data = json.loads(body)
    for field, value in data.items():
        setattr(f, field, value)
    f.save()
    return HttpResponse(status=HTTPStatus.NO_CONTENT)


def handle_detail_delete(pk):
    # Question 5: Complete this function body
    f = get_object_or_404(Fruit, pk=pk)
    f.delete()
    return HttpResponse(status=HTTPStatus.NO_CONTENT)
```

### handle_detail_put
- You do not need to import any additional modules
- Get the Fruit object based on pk or a 404 response if it does not exist
- Convert the string into JSON
- Iterate over each item in the JSON object, updating the fields with the new values
- Save the updated Fruit object
- Return a 204 status code

### handle_detail_delete
- You do not need to import any additional modules
- Get the Fruit object based on pk or a 404 response if it does not exist
- Delete this Fruit object
- Return a 204 status code