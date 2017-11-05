from django.db import models
from django.utils import timezone


class Book(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    descriptions = models.TextField()
    published_date = models.DateField(
            blank=True, null=True)
    genre = models.CharField(max_length=100)
    def __str__(self):
        return self.title