from django.db import models

class UrlShortener(models.Model):

    code = models.CharField(max_length=10)
    url = models.CharField(max_length=200)
    
    def __str__(self):
        return self.code