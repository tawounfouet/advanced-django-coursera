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