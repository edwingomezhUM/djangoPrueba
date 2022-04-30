from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.

class tracks(models.Model):

    id = models.IntegerField(primary_key=True)
    artistName = models.TextField()
    name = models.TextField()
    kind = models.TextField()
    artistId = models.TextField()
    artistUrl = models.TextField()
    contentAdvisoryRating = models.TextField()
    artworkUrl100 = models.TextField()
    url = models.TextField()

class genres(models.Model):

    genreId = models.IntegerField()
    name = models.TextField()
    url = models.TextField()