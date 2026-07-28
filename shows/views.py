from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Session
from .serializers import SessionSerializer
from halls.models import Seat
from bookings.models import Booking
from users.permissions import IsAdminUser

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Session.objects.all()
        movie_id = self.request.query_params.get('movie')
        if movie_id:
            queryset = queryset.filter(movie_id=movie_id)
        return queryset

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAdminUser()]
        return super().get_permissions()

    @action(detail=True, methods=['get'])
    def seats(self, request, pk=None):
        session = self.get_object()
        seats = Seat.objects.filter(hall=session.hall)
        booked = Booking.objects.filter(session=session).values_list('seat_id', flat=True)
        data = [{
            'id': seat.id,
            'row': seat.row,
            'number': seat.number,
            'is_booked': seat.id in booked,
            'seat_type': seat.seat_type
        } for seat in seats]
        return Response(data)
