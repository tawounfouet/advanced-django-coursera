# Django Rest Framework Serializers and Views: Question 3
Question 3
Sessions can only be booked in 5-minute increments. Any request session_length should be rounded down to the nearest 5 minutes. For example, 49 minutes becomes 45, 44 to 40, etc. 5, 10, 15, 20, 25, and so on, stay unchanged. Implement a validate_session_length() method to achieve this. Hint, the Python function math.floor() will be handy here.


## Solution GPT

```python
from rest_framework import serializers
import math

from assessment.models import AppointmentRequest


def validate_full_name(value):
    if " " not in value:
        raise serializers.ValidationError(
            "Name must have first and last name(s) separated by space(s)."
        )


class AppointmentRequestSerializer(serializers.Serializer):
    stylist_name = serializers.CharField(max_length=70, validators=[validate_full_name])
    start_datetime = serializers.DateTimeField()
    session_length = serializers.IntegerField(min_value=5, max_value=60, required=False)

    def validate_session_length(self, value):
        # Round down to the nearest 5 minutes
        return int(math.floor(value / 5.0) * 5)

    def create(self, validated_data):
        return AppointmentRequest(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        return instance

```

## Solution Codio

```python
# Question 3 & 4: Add any imports you need
from math import floor
from rest_framework import serializers

from assessment.models import AppointmentRequest


def validate_full_name(value):
    # Question 2: Complete this function
    if " " not in value:
        raise serializers.ValidationError(
            "Name must have first and last name(s) separated by space(s)."
        )

    return value


class AppointmentRequestSerializer(serializers.Serializer):
    # Question 1 & 2: Create and edit fields
    stylist_name = serializers.CharField(max_length=70, validators=[validate_full_name])
    start_datetime = serializers.DateTimeField()
    session_length = serializers.IntegerField(min_value=5, max_value=60, required=False)

    # Question 3: Implement validation method
    @staticmethod
    def validate_session_length(value):
        return 5 * floor(value / 5)

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

- Import floor from the math module.
- Create the validate_session_length method; use the static method decorator.
- Find the floor of value divided by 5, then return this multiplied by 5.