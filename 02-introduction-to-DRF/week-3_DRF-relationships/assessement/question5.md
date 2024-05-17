# Django Rest Framework Relationships: Question 5

## Question 5
This carries on from Question 4. Update the CustomerSerializer so that the nested address is writable. Addresses should only be created if they don’t already exist, (i.e. the street_name/city combination is unique).

```python
from rest_framework import serializers

# Question 3, 4, 5: Add any imports you need
from bakery.api.assessment_serializers import AddressSerializer
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
    address = AddressSerializer()

    class Meta:
        model = Customer
        fields = "__all__"

    # Question 5: Implement your methods here
```


## Solution
```python
from rest_framework import serializers

# Question 3, 4, 5: Add any imports you need
from bakery.api.assessment_serializers import AddressSerializer
from bakery.models import Food, Customer, Order, Address


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
    address = AddressSerializer()

    class Meta:
        model = Customer
        fields = "__all__"

    # Question 5: Implement your methods here

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

## Create Method
- Import Address
- Pull out the address dictionary from validated_data
- Create an Address object with the object
- Put the newly created address back into validated_data
- Create a new Customer object with the updated validated_data

## Update Method
- Check if either the city or street name of instance do not match those in validated_data
- If yes, create a new Address object with validated_data
- Set instance.address to the new Address object
- Save the change to instance