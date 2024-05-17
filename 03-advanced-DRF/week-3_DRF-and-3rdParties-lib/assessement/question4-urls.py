"""module3 URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

# Question 4: Add you imports here
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from assessment.views import PostViewSet, WhoAmIView

router = DefaultRouter()
router.register("posts", PostViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("rest_framework.urls")),
    path("api/v1/token-auth/", views.obtain_auth_token),
    path("api/v1/whoami/", WhoAmIView.as_view()),
    path("api/v1/", include(router.urls)),
    # Question 4: Add your URL patterns here
    path("api/v1/jwt/", TokenObtainPairView.as_view()),
    path("api/v1/jwt/refresh/", TokenRefreshView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)