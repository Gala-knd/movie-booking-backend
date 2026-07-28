from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from movies.models import Movie
from halls.models import Hall

class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    price_vip = models.DecimalField(max_digits=8, decimal_places=2)
    price_regular = models.DecimalField(max_digits=8, decimal_places=2)

    def clean(self):
        if self.start_time < timezone.now():
            raise ValidationError({'start_time': 'Сеанс не может быть в прошлом'})
        if self.price_vip < 0 or self.price_regular < 0:
            raise ValidationError('Цены не могут быть отрицательными')
        if self.price_vip < self.price_regular:
            raise ValidationError('Цена VIP не может быть меньше обычной')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.movie.title} - {self.start_time}"
