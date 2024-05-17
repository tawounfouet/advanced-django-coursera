# Question 5: Add imports here
from rest_framework import generics

from assessment.models import Stylist
from assessment.serializers import StylistSerializer


# Question 5: Update the class to inherit correctly
class StylistList(generics.ListCreateAPIView):
    # Question 5: Add attributes
    queryset = Stylist.objects.all()
    serializer_class = StylistSerializer


# Question 5: Update the class to inherit correctly
class StylistDetail(generics.RetrieveUpdateDestroyAPIView):
    # Question 5: Add attributes
    queryset = Stylist.objects.all()
    serializer_class = StylistSerializer