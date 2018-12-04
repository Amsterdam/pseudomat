from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=150)
    secret = models.CharField(max_length=150)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name
