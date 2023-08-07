from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.CharField(max_length=200)

    def __str__(self):
        return f"name: {self.name} , email: {self.email}, message: {self.message}"
