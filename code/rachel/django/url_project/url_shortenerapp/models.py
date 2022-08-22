from django.db import models

class Store(models.Model):
    long_url = models.CharField(max_length=255)
    short_url = models.CharField(max_length=6)
    
    def __str__(self):
        return self.long_url
