from django.db import models
from django.contrib.auth import get_user_model

class Student(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    cohort = models.CharField(max_length=25)
    favorite_topic = models.CharField(max_length=25)
    favorite_teacher = models.CharField(max_length=25)
    capstone = models.URLField

    def __str__(self):
        return self.first_name, self.last_name

    class Meta:
        ordering = ['-last_name']
# Create your models here.
