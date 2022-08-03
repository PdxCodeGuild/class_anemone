from django.db import models
from django.forms import URLField

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cohort = models.CharField(max_length=50)
    favorite_topic = models.CharField(max_length=100)
    favorite_teacher = models.CharField(max_length=100)
    capstone = models.URLField(max_length=200)
    create_date_time = models.DateTimeField(auto_now_add=True)
    update_date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['-create_date_time']    
