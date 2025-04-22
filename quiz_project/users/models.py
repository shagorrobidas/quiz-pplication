from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_participant = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    
    def __str__(self):
        return self.username