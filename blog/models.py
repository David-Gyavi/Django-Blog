from django.db import models
from django.utils import timezone

class Musician(models.model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=50)
    post_created = models.DateTimeField(default=timezone.now())

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = model.IntegerField()    
