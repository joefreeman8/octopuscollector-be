"""
URL configuration for octopuscollector project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from main_app import views

# Create main router
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'octopus', views.OctopusViewSet)

# Create a nested router for the octopus
# * installed "pip install drf-nested-routers"
octopus_router = routers.NestedSimpleRouter(
    router, r'octopus', lookup='octopus')
octopus_router.register(
    r'sightings', views.SightingViewSet, basename='octopus-sightings')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include(octopus_router.urls)),
]
