from django.db import models

# Create your models here.
class Url(models.Model):
    url = models.CharField(max_length=200)
    slug = models.CharField(max_length=15)