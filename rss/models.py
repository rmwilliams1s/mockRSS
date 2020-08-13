from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User


# class User(models.Model):
#     username = models.CharField(max_length=30, unique=True)
#     password = models.CharField(max_length=30)

#     def __str__(self):
#         return self.username

class RSS(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=100, default="N/A")
    date = models.CharField(max_length=50, default="N/A")
    description = models.CharField(max_length=500, default="N/A")
    image = models.URLField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
