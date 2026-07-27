from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Hall, Seat
from .serializers import HallSerializer, SeatSerializer
from users.permissions import IsAdminUser

class HallListCreateView(generics.ListCreateAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]

class HallRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]
