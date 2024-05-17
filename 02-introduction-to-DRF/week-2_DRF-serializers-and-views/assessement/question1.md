
# Django Rest Framework Serializers and Views: Question 1

## Question 1
In the models.py file is the class AppointmentRequest. This is not a Django model as the intended use is that an API client could send an AppointmentRequest body which would then be processed further. For example, maybe the backend would send an email or pass it on to a calendaring system. Regardless, it’s only a transport format, and not stored in the database.
Your first task is to add the three serializer fields on the AppointmentRequestSerializer class. stylist_name should have a maximum length of 70 characters. The datetime field should contain the date and time of the appointment. session_length should have a minimum value of 5 and maximum value of 60. This field is not required as we provide a default in the AppointmentRequest class.


## Task
```python
from rest_framework import serializers
from assessment.models import AppointmentRequest

# Question 3 & 4: Add any imports you need



def validate_full_name(value):
    # Question 2: Complete this function
    return value


class AppointmentRequestSerializer(serializers.Serializer):
    # Question 1 & 2: Create and edit fields

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

## Solution GPT

```python
from rest_framework import serializers
from assessment.models import AppointmentRequest

# Question 3 & 4: Add any imports you need
from rest_framework.validators import MinValueValidator, MaxValueValidator

def validate_full_name(value):
    # Question 2: Complete this function
    return value

class AppointmentRequestSerializer(serializers.Serializer):
    # Question 1 & 2: Create and edit fields
    stylist_name = serializers.CharField(max_length=70)
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
    return value


class AppointmentRequestSerializer(serializers.Serializer):
    # Question 1 & 2: Create and edit fields
    stylist_name = serializers.CharField(max_length=70)
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

- Add stylist_name as a CharField with a max length of 70.
- Add start_datetime as a DateTimeField.
- Add session_length as an IntegerField. The minimum length is 5 and the max length is 60. This field is not required.