from django.db import models
from movies.models import Movie
from halls.models import Hall

class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    price_vip = models.DecimalField(max_digits=8, decimal_places=2)
    price_regular = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.movie.title} - {self.start_time}"
