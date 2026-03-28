from django.db import models
from django.contrib.auth.models import AbstractUser

class PicturaUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.jpg', blank=True)

    def __str__(self):
        return self.username
    