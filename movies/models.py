from django.db import models 
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title()
