"""module4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from bakery.api.assessment_views import Question1View

# Question 2: Add any imports you need
from rest_framework.routers import DefaultRouter
from bakery.api import views as api_views

# Question 2: Configure the router
router = DefaultRouter()
router.register("orders", api_views.OrderViewSet)
router.register("addresses", api_views.AddressViewSet)
router.register("food", api_views.FoodViewSet)
router.register("customers", api_views.CustomerViewSet)

api_patterns = [
    path("question1/", Question1View.as_view()),
    # Question 2: add the router URLs
    path("", include(router.urls)),
]

urlpatterns = [path("admin/", admin.site.urls), path("api/v1/", include(api_patterns))]