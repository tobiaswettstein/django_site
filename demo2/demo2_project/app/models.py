from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=128)
    blog = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    public_gists = models.CharField(max_length=128)
    public_repos = models.CharField(max_length=128)
    avatar_url = models.ImageField()
    followers = models.CharField(max_length=128)
    following = models.CharField(max_length=128)