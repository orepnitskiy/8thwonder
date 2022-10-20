from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TwitterTokens(models.Model):
    token = models.CharField(max_length=255)

class InstagramTokens(models.Model):
    token = models.CharField(max_length=255)

class Group(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    users_amount = models.IntegerField()
    token = models.CharField(max_length=255)