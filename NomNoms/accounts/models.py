from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Create your models here.

class CustomUser(AbstractUser):
    '''email = models.EmailField(max_length=30)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=30)'''
    pass

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='following', blank=True) #relatedname allows reverse access
    preferences = models.JSONField(default=dict, blank=True) #leaving this as JSON for now, can decide how dietpref shld be stored later

    def __str__(self):
        return f"{self.user.username}'s profile"