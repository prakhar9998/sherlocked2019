from django.db import models
from django.contrib.auth.models import AbstractUser

class Player(AbstractUser):
    zeal_Id = models.CharField(max_length=200)
    level = models.IntegerField(default =0)
    time_delta = models.DateTimeField(null=True)
