from __future__ import unicode_literals
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=128)
    dialogues = models.ManyToManyField('Dialogues')


class Dialogues(models.Model):
    dialogue = models.TextField()
    movie_name = models.CharField(max_length=128)
    star = models.CharField(max_length=128)
    movie_year = models.IntegerField(default=1950)
    poster = models.TextField()


class Emotion(models.Model):
    dialogue = models.ForeignKey("Dialogues")
    mood = models.CharField(max_length=128)
    count = models.IntegerField(default=1)
