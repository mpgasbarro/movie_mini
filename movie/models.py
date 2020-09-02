from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    photo_url = models.TextField()
    actors = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models. TextField()

    def __str__(self):
        return f'{self.title}, {self.director}, {self.photo_url}, {self.actors}, {self.genre}, { self.description}'