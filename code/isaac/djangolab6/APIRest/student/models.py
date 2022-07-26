from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100)  # First name attribute.  Max length will be 100 chars.
    last_name = models.CharField(max_length=100)   # Last name attribute.  Max length will be 100 chars.
    cohort = models.TextField(max_length=500)      # Cohort attribute.  Max length will be 500 chars.
    favorite_topic = models.CharField(max_length=50)   # Fav Topic att.  Max length 50 chars.
    favorite_teacher = models.CharField(max_length=100)    # Fav Teacher att.  Max length 100 chars.
    capstone = models.URLField(max_length=300)   # Capstone with a URLField.

    def __str__(self):
        return self.first_name, self.last_name
