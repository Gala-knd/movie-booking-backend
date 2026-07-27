from rest_framework import serializers
from .models import Hall, Seat

class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = '__all__'

class SeatSerializer(serializers.ModelSerializer):
    hall = HallSerializer(read_only=True)

    class Meta:
        model = Seat
        fields = '__all__'
