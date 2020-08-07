from django.db import models
from django.utils import timezone


class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class RSS(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=100, default="N/A")
    date = models.DateTimeField(default=timezone.now())
    description = models.CharField(max_length=500, default="N/A")
    image = models.URLField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
