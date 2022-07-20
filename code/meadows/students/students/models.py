from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    cohort = models.CharField(max_length=300)
    favorite_topic = models.CharField(max_length=300)
    favorite_teacher = models.CharField(max_length=300)
    capstone = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name
