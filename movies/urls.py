from django.urls import path
from .views import MovieListCreateView, MovieRetrieveUpdateDestroyView

urlpatterns = [
    path('', MovieListCreateView.as_view(), name='movie-list'),
    path('<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail'),
]
