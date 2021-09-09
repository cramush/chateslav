from django.db import models
from datetime import datetime, timedelta


class Room(models.Model):
    name = models.CharField(max_length=1000)


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now() + timedelta(hours=3), blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
