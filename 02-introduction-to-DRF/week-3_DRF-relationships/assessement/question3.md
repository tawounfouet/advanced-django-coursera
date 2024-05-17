# Django Rest Framework Relationships: Question 3

## Question 3
The Order API (at /api/v1/orders) uses the OrderSerializer in bakery/api/serializers.py. Make changes to this serializer so that the food list is displayed as strings rather than IDs. This list should be writable too, using the name of the food.


## Task
```python
from rest_framework import serializers

# Question 3, 4, 5: Add any imports you need
from bakery.models import Customer, Order


class OrderSerializer(serializers.ModelSerializer):
    # Question 3: Add your fields here

    class Meta:
        model = Order
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    # Question 4: Add your fields here

    class Meta:
        model = Customer
        fields = "__all__"

    # Question 5: Implement your methods here

```



## Solution
```python
from rest_framework import serializers

# Question 3, 4, 5: Add any imports you need
from bakery.models import Food, Customer, Order


class OrderSerializer(serializers.ModelSerializer):
    # Question 3: Add your fields here
    food = serializers.SlugRelatedField(
        slug_field="name", many=True, queryset=Food.objects.all()
    )

    class Meta:
        model = Order
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    # Question 4: Add your fields here

    class Meta:
        model = Customer
        fields = "__all__"

    # Question 5: Implement your methods here
```

- Import Food
- Set food to a SlugRelatedField
- Set slug_field to name, many to True, and queryset to all of the Food objects


