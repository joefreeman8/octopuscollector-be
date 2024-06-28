from django.urls import path
from .views import OctopusListView, OctopusDetailView

urlpatterns = [
    path('', OctopusListView.as_view()),
    path('<int:pk>/', OctopusDetailView.as_view())
]