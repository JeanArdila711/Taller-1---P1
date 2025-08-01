from django.db import models
from django.contrib.auth.models import User 

class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    image = models.ImageField(upload_to='movies/')

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    watch_again = models.BooleanField(default=False)

class News(models.Model):
    headline = models.CharField(max_length=200)
    story = models.TextField()
    date = models.DateField()
