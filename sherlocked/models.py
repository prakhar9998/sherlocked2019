from django.contrib.auth.models import AbstractUser
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_story = models.TextField()
    question_level = models.IntegerField(default=-1)
    answer = models.CharField(max_length=100)