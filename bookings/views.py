from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from .models import Booking
from .serializers import BookingSerializer
from halls.models import Seat
from shows.models import Session
import uuid

class BookingListCreateView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        session_id = self.request.data.get('session')
        seat_id = self.request.data.get('seat')
        session = get_object_or_404(Session, id=session_id)
        seat = get_object_or_404(Seat, id=seat_id)

        if Booking.objects.filter(session=session, seat=seat).exists():
            raise serializers.ValidationError("Это место уже занято")

        booking_code = str(uuid.uuid4())[:8]
        booking = serializer.save(user=self.request.user, booking_code=booking_code)
        booking.generate_qr()
        booking.save()

class BookingRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
