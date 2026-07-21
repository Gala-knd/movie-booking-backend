from django.urls import path
from .views import SessionListCreateView, SessionRetrieveUpdateDestroyView

urlpatterns = [
    path('', SessionListCreateView.as_view(), name='session-list'),
    path('<int:pk>/', SessionRetrieveUpdateDestroyView.as_view(), name='session-detail'),
]
