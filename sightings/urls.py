from django.urls import path
from .views import SightingListView

urlpatterns = [
    path('', SightingListView.as_view()),
    # path('<int:pk>/', OctopusDetailView.as_view())
]