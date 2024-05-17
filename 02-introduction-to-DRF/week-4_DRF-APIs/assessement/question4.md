# Django Rest Framework APIs: Question 4

## Question 4
We would like to have different serializer classes for OrderViewSet, depending on the action. For a list action, the OrderViewSet should use the OrderListSerializer, otherwise, use the OrderDetailSerializer. The OrderListSerializer does not include the food in its serialized output, whereas the OrderDetailSerializer does.


```python
from rest_framework import viewsets

from bakery.models import Order, Food, Customer, Address


# Questions 3, 4 and 5: Add your imports here
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
    

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    # Question 3: Complete the class attributes
    serializer_class = AddressSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    # Question 3: Complete the class attributes
    serializer_class = FoodSerializer
```

- Import OrderListSerializer and OrderDetailSerializer
- Define get_serializer_class
- If self.action is "list" then return OrderListSerializer
- If not, return OrderDetailSerializer