from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'session', 'seat', 'user', 'booking_code', 'is_paid', 'booked_at', 'qr_code']
        read_only_fields = ['user', 'booking_code', 'is_paid', 'booked_at', 'qr_code']
