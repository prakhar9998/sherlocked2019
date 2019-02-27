from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.validators import RegexValidator

class Player(AbstractUser):
    zeal_Id = models.CharField(max_length=200)
    level = models.IntegerField(default=1)
    unlock_time = models.DateTimeField(default=timezone.now)
    last_solved = models.DateTimeField(default=timezone.now)
    contact_regex = RegexValidator(regex=r'^[1-9]\d{9}$',
        message="Phone number should be of 10 digits.")
    contact_no = models.CharField(validators=[contact_regex], max_length=10, blank=True)
    college_name = models.CharField(max_length=100, null=True)