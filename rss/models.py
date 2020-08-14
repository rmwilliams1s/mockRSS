from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User


# Store information about each post along w/ current user
class RSS(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=100, default="N/A")
    date = models.DateTimeField()
    description = models.CharField(max_length=500, default="N/A")
    image = models.URLField(blank=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)



class SortFeedForm(forms.Form):
    SORT_CHOICES = [
    ('date_desc', 'Date: Newest to Oldest'),
    ('date_asc', 'Date: Oldest to Newest'),
    ('title_asc', 'Title: A-Z'),
    ('title_desc', 'Title: Z-A'),
    ('description', 'Description containing:')
    ]

    choice = forms.CharField(
label='Sort by:', widget=forms.Select(choices=SORT_CHOICES), required=False)
    keyword = forms.CharField(max_length=500, required=False)
