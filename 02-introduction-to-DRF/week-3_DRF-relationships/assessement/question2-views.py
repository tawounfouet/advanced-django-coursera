# views.py
from bakery.api.assessment_views import NameAndCountBaseView

# Question 2: Add any imports you need here
from bakery.api.permissions import InversePermissions


class NameAndCountView(NameAndCountBaseView):
    # Question 2: Make changes to this class to configure permissions
    permission_classes = [InversePermissions]