from rest_framework import serializers
from .models import Booking
from shows.serializers import SessionSerializer
from halls.serializers import SeatSerializer

class BookingSerializer(serializers.ModelSerializer):
    session = SessionSerializer(read_only=True)
    seat = SeatSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'session', 'seat', 'user', 'booking_code', 'is_paid', 'booked_at', 'qr_code']
        read_only_fields = ['user', 'booking_code', 'is_paid', 'booked_at', 'qr_code']
