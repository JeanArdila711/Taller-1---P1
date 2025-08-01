from django.contrib import admin
from .models import Movie, News, Review

# Register your models here.
admin.site.register(Movie)
admin.site.register(News)
admin.site.register(Review)
