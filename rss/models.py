from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class RSS(models.Model):
    url = models.URLField()
    # title = models.CharField(max_length=100)
    # date = models.DateTimeField()
    # description = models.CharField(max_length=500)
    # image = models.URLField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
