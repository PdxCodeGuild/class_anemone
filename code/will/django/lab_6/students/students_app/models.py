from django.db import models

class Student(models.Model):
    firstname = models.CharField(max_length=120)
    lastname = models.CharField(max_length=120)
    cohort = models.CharField(max_length=120)
    favorite_topic = models.CharField(max_length=120)
    favorite_teacher = models.CharField(max_length=120)
    capstone = models.URLField

    def __str__(self):
        return self.lastname

