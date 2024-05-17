# Question 3

Now, fill in the bodies of the get functions, handle_detail_get and handle_list_get. In assessment/models.py a function for converting a Fruit object to a dictionary has been provided: fruit_to_dict. You can use this to create JSON responses. For the detail get, return a single dictionary representing the Fruit, and make sure django.http.Http404 is raised if a Fruit with the specified pk is not found.

For the list get, return a list of dictionaries, nested in a dictionary, under the data key.
Django Admin has been configured for the Fruit model so you can use it to create Fruit objects for testing.


## Solution GPT

```python
def handle_list_get():
    # Question 3: Complete this function body
    fruits = Fruit.objects.all()
    fruit_list = [fruit_to_dict(fruit) for fruit in fruits]
    return JsonResponse({"data": fruit_list})

def handle_detail_get(pk):
    # Question 3: Complete this function body
    try:
        fruit = Fruit.objects.get(pk=pk)
        fruit_dict = fruit_to_dict(fruit)
        return JsonResponse(fruit_dict)
    except Fruit.DoesNotExist:
        raise Http404("Fruit not found")

```

## Solution - Codio 
```python
def handle_list_get():
    # Question 3: Complete this function body
    return JsonResponse({"data": list(map(fruit_to_dict, Fruit.objects.all()))})

def handle_detail_get(pk):
    # Question 3: Complete this function body
    f = get_object_or_404(Fruit, pk=pk)
    return JsonResponse(fruit_to_dict(f))

```
### handle_list_get
- Pass each Fruit object to the fruit_to_dict function
- Store each dictionary from Fruit object in a list
- Use JsonResponse to convert a list of dictionaries to JSON

### handle_detail_get
- Use pk to select a specific Fruit object
- Use get_object_or_404 so a 404 status is returned if the object does not exist
- Use JsonResponse to return the details of the Fruit object as JSON