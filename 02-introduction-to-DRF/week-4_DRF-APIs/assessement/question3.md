# Django Rest Framework APIs: Question 3

## Question 3
The OrderViewSet, AddressViewSet, FoodViewSet and CustomerViewSet have been partially configured but need to have their serializers set up. The serializer classes have already been implemented for you in bakery/api/assessment_serializers.py.
Note that in Question 4 we will update OrderViewSet to have varying serializers, but for now just use the OrderSerializer class on OrderViewSet.
Once you’ve completed the viewsets you’ll be able to test them via the DRF GUI. The first thing to do is migrate the changes.

### MIGRATIONS
Then run create_fixtures command. This will generate a list of food at /api/v1/food/, or individual food items like /api/v1/food/1/. It will do the same thing for orders, addresses and customers.

### CREATE FIXTURES
Finally, you can launch the dev server and open the website.
START DEV SERVER

### View API


## Task

```python
# views 
from rest_framework import viewsets

from bakery.models import Order, Food, Customer, Address


# Questions 3, 4 and 5: Add your imports here


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    # Question 3: Complete the class attributes

    # Question 4: Add your new method here


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    # Question 3: Complete the class attributes

    # Question 5: Add your new method here


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    # Question 3: Complete the class attributes


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    # Question 3: Complete the class attributes
```


```python
# assessement.py
# This file does not need to be edited

from rest_framework import serializers

from bakery.models import Address, Food, Order, Customer


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

    def create(self, validated_data):
        return Address.objects.get_or_create(**validated_data)[0]

    def update(self, instance, validated_data):
        return Address.objects.get_or_create(**validated_data)[0]


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "customer"]


# An alias for Question 3 or 4, it doesn't matter which of these names is used
OrderListSerializer = OrderSerializer


class OrderDetailSerializer(serializers.ModelSerializer):
    food = serializers.SlugRelatedField(
        slug_field="name", many=True, queryset=Food.objects.all()
    )

    class Meta:
        model = Order
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Customer
        fields = "__all__"

    def create(self, validated_data):
        address_dict = validated_data.pop("address")
        address = Address.objects.get_or_create(**address_dict)[0]
        validated_data["address"] = address
        return super(CustomerSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        address_dict = validated_data.pop("address")
        super(CustomerSerializer, self).update(instance, validated_data)

        if (
            instance.address.street_name != address_dict["street_name"]
            or instance.address.city != address_dict["city"]
        ):
            address = Address.objects.get_or_create(**address_dict)[0]
            instance.address = address
            instance.save()

        return instance
```


## Solution
```python
from rest_framework import viewsets


from bakery.models import Order, Food, Customer, Address


# Questions 3, 4 and 5: Add your imports here
from bakery.api.assessment_serializers import (
    AddressSerializer,
    FoodSerializer,
    OrderSerializer,
    CustomerSerializer,
)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    # Question 3: Complete the class attributes
    serializer_class = OrderSerializer

    # Question 4: Add your new method here
    

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    # Question 3: Complete the class attributes
    serializer_class = CustomerSerializer

    # Question 5: Add your new method here
    

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    # Question 3: Complete the class attributes
    serializer_class = AddressSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    # Question 3: Complete the class attributes
    serializer_class = FoodSerializer
```

- Import OrderSerializer, CustomerSerializer, AddressSerializer, and FoodSerializer
- For OrderViewSet, assign OrderSerializer to the variable serializer_class
- For CustomerViewSet, assign CustomerSerializer to the variable serializer_class
- For AddressViewSet, assign AddressSerializer to the variable serializer_class
- For FoodViewSet, assign FoodSerializer to the variable serializer_class