from django.db import models

# Create your models here.


class Announcement(models.Model):
    title = models.CharField(max_length=256)
    day = models.CharField(max_length=10)
    time = models.CharField(max_length=6)
    channel = models.CharField(max_length=32)
    message = models.CharField(max_length=4096)
