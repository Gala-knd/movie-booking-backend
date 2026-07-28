from django.db import models
from django.core.exceptions import ValidationError

class Hall(models.Model):
    name = models.CharField(max_length=100)
    rows = models.IntegerField()
    seats_per_row = models.IntegerField()
    is_active = models.BooleanField(default=False)

    def clean(self):
        if self.rows < 1 or self.rows > 50:
            raise ValidationError({'rows': 'Количество рядов должно быть от 1 до 50'})
        if self.seats_per_row < 1 or self.seats_per_row > 20:
            raise ValidationError({'seats_per_row': 'Количество мест в ряду должно быть от 1 до 20'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

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
