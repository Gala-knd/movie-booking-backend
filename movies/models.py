from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.IntegerField()
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)
    release_date = models.DateField()

    def __str__(self):
        return self.title
