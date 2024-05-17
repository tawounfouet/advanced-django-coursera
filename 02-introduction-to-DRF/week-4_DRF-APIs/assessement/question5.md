# Django Rest Framework APIs: Question 5

## Question 5
Add another method to the CustomerViewSet that will return a response containing the orders for the current customer. The method should be called orders, which means it will be accessible at the path /api/v1/customers/<pk>/orders/ where <pk> is a number representing the customer. Even though we will be serializing many orders, use the OrderDetailSerializer so the customer can see the food that’s in each of their orders.


## Solution
```python
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


## Solution

```python
from rest_framework import viewsets
from bakery.models import Order, Food, Customer, Address

# Questions 3, 4 and 5: Add your imports here
from rest_framework.decorators import action
from rest_framework.response import Response
from bakery.api.assessment_serializers import (
    AddressSerializer,
    FoodSerializer,
    OrderSerializer,
    OrderListSerializer,
    OrderDetailSerializer,
    CustomerSerializer,
)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    # Question 3: Complete the class attributes
    serializer_class = OrderSerializer

    # Question 4: Add your new method here
    def get_serializer_class(self):
        if self.action == "list":
            return OrderListSerializer
        return OrderDetailSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    # Question 3: Complete the class attributes
    serializer_class = CustomerSerializer

    # Question 5: Add your new method here
    @action(detail=True)
    def orders(self, request, pk=None):
        customer = self.get_object()
        serializer = OrderDetailSerializer(customer.order_set, many=True)
        return Response(serializer.data)


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    # Question 3: Complete the class attributes
    serializer_class = AddressSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    # Question 3: Complete the class attributes
    serializer_class = FoodSerializer
```

- Define the orders method
- Use the action decorator
- Set customer to self.get_object()
- Set serializer to OrderDetailSerializer(customer.order_set, many=True)
- Return Response(serializer.data)