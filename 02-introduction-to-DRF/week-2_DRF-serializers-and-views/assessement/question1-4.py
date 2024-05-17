# Question 3 & 4: Add any imports you need
from math import floor
from rest_framework import serializers

from assessment.models import AppointmentRequest, Stylist

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
    class Meta():
        model = Stylist
        fields = "__all__"