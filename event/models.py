from pickle import TRUE
from turtle import title
from django.db import models
from datetime import datetime

# Create your models here.
class Events(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(default=datetime.now)
    time = models.TimeField(default=datetime.now)
    venue = models.CharField(max_length=400)
    description = models.TextField()
    email = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")
    id = models.IntegerField(primary_key=TRUE)

    def __str__(self) -> str:
        return self.title