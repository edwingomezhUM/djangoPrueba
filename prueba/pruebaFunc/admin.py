from pyexpat import model
from django.contrib import admin
from .models import tracks, genres

# Register your models here.

admin.site.register(tracks)
admin.site.register(genres)
