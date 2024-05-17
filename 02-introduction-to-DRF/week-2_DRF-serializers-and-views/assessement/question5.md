# Django Rest Framework Serializers and Views: Question 5

## Question 5
The StylistList and StylistDetail view classes have been created in views.py. There are URL patterns set up to point to them too, stylists/ and stylists/<int:pk> respectively. However these views need to be implemented using Django Rest Framework generic. Currently they inherit from the base Django View class. The inheritance needs to be changed to inherit from DRF generic classes, and the right attributes need to be added to each. Hint, you don’t need to write any methods, just add two attributes to each class.



## Task
```python
# Question 5: Add imports here
from django.views import View


# Question 5: Update the class to inherit correctly
class StylistList(View):
    # Question 5: Add attributes
    pass


# Question 5: Update the class to inherit correctly
class StylistDetail(View):
    # Question 5: Add attributes
    pass
```

## Solution
```python
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
```

- Import generics from rest_framework.
- Import the Stylist model.
- Import the serializer StylistSerializer.
- For StylistList, inherit from generics.ListCreateAPIView.
- For StylistDetail, inherit from generics.RetrieveUpdateDestroyAPIView.
- For both classes, set queryset to all of the Stylist objects.
- For both classes, set serializer_class to StylistSerializer.