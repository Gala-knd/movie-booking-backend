from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def validate_duration(self, value):
        if value <= 0:
            raise serializers.ValidationError("Длительность должна быть больше 0")
        return value

    def validate_title(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Название не может быть пустым")
        return value
