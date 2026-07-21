from django.urls import path
from .views import BookingListCreateView, BookingRetrieveDestroyView

urlpatterns = [
    path('', BookingListCreateView.as_view(), name='booking-list'),
    path('<int:pk>/', BookingRetrieveDestroyView.as_view(), name='booking-detail'),
]
