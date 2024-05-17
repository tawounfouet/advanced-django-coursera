# Django Rest Framework Serializers and Views: Question 2
Question 2

We want to ensure that the stylist’s name contains both first and last names, i.e. that it contains a space anywhere in it. Complete the validate_full_name() function in serializers.py to add this check, and raise an appropriate exception if the name is not valid. Then, add this validator function to the stylist_name field.
TRY



## Solution GPT

```python
from rest_framework import serializers
from assessment.models import AppointmentRequest

# Question 3 & 4: Add any imports you need
from rest_framework.validators import MinValueValidator, MaxValueValidator

def validate_full_name(value):
    # Question 2: Complete this function
    if ' ' not in value:
        raise serializers.ValidationError("The stylist's name must contain both a first and last name.")
    return value

class AppointmentRequestSerializer(serializers.Serializer):
    # Question 1 & 2: Create and edit fields
    stylist_name = serializers.CharField(
        max_length=70,
        validators=[validate_full_name]
    )
    datetime = serializers.DateTimeField()
    session_length = serializers.IntegerField(
        required=False,
        validators=[MinValueValidator(5), MaxValueValidator(60)]
    )

    # Question 3: Implement validation method
    def create(self, validated_data):
        return AppointmentRequest(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        return instance

class StylistSerializer(serializers.ModelSerializer):
    # Question 4: Implement this serializer
    pass

```

## Solution Codio

```python
# Question 3 & 4: Add any imports you need
from rest_framework import serializers

from assessment.models import AppointmentRequest


def validate_full_name(value):
    # Question 2: Complete this function
    if " " not in value:
        raise serializers.ValidationError(
            "Name must have first and last name(s) separated by space(s)."
        )


class AppointmentRequestSerializer(serializers.Serializer):
    # Question 1 & 2: Create and edit fields
    stylist_name = serializers.CharField(max_length=70, validators=[validate_full_name])
    start_datetime = serializers.DateTimeField()
    session_length = serializers.IntegerField(min_value=5, max_value=60, required=False)

    # Question 3: Implement validation method

    def create(self, validated_data):
        return AppointmentRequest(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        return instance


class StylistSerializer(serializers.ModelSerializer):
    # Question 4: Implement this serializer
    pass
```

- In the validate_full_name function, determine if a space is not in value (which corresponds to stylist_name).
- If a space is missing, raise a serializers.ValidationError.
- The raised error should contain a message that lets the user know that a space is missing.
- Add the validate function to the stylist_name field.