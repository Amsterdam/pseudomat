from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=150)
    secret = models.CharField(max_length=150, null=True, blank=True)
    vao_ip = models.CharField(max_length=150, null=True)
    upload_dir = models.CharField(max_length=256, null=True)
    users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name


