from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Player(AbstractUser):
    zeal_Id = models.CharField(max_length=200)
    level = models.IntegerField(default=1)
    unlock_time = models.DateTimeField(default=timezone.now)
    last_solved = models.DateTimeField(default=timezone.now)
