from rest_framework import serializers
from .models import Session
from movies.serializers import MovieSerializer
from halls.serializers import HallSerializer

class SessionSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    hall = HallSerializer(read_only=True)

    class Meta:
        model = Session
        fields = '__all__'
