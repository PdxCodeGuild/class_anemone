from django.db import models
import random

class ShortUrl(models.Model):
    code = models.CharField(max_length=6)
    url = models.CharField(max_length=500)

    def __str__(self):
        return self.url
