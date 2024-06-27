from django.urls import path
from .views import OctopusListView

urlpatterns = [
    path('', OctopusListView.as_view()),
]