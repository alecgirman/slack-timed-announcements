from django.db import models

# Create your models here.

day_list = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
DAYS = [(d, d) for d in day_list]

channel_list = ["general", "bot-testing"]

CHANNELS = [(c, c) for c in channel_list]


class Announcement(models.Model):
    title = models.CharField(max_length=256)
    day = models.CharField(max_length=10, choices=DAYS)
    time = models.TimeField()
    channel = models.CharField(max_length=32, choices=CHANNELS)
    message = models.CharField(max_length=4096)
