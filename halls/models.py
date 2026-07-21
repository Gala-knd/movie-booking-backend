from django.db import models

class Hall(models.Model):
    name = models.CharField(max_length=100)
    rows = models.IntegerField()
    seats_per_row = models.IntegerField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Seat(models.Model):
    TYPES = (('regular', 'Обычное'), ('vip', 'VIP'))
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='seats')
    row = models.IntegerField()
    number = models.IntegerField()
    seat_type = models.CharField(max_length=10, choices=TYPES, default='regular')

    class Meta:
        unique_together = ('hall', 'row', 'number')
