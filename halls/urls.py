from django.urls import path
from .views import HallListCreateView, HallRetrieveUpdateDestroyView

urlpatterns = [
    path('', HallListCreateView.as_view(), name='hall-list'),
    path('<int:pk>/', HallRetrieveUpdateDestroyView.as_view(), name='hall-detail'),
]
