from django.db import models 
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    pass

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255, null=True, blank=True)
    year = models.CharField(max_length=4, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


