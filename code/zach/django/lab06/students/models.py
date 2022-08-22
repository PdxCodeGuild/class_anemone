from django.db import models

class Student(models.Model):
    f_name = models.CharField(max_length=200)
    l_name = models.CharField(max_length=200)
    cohort = models.CharField(max_length=200)
    fav_topic = models.CharField(max_length=200)
    fav_teacher = models.CharField(max_length=200)
    capstone = models.URLField(help_text='student capstone project URL')
    
    def __str__(self) -> str:
        return self.l_name
