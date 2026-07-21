from rest_framework import generics
from .models import Hall, Seat
from .serializers import HallSerializer, SeatSerializer

class HallListCreateView(generics.ListCreateAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer

class HallRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
