from django.db import models

# Create your models here.

#model to store long and short urls
class UrlShortener(models.Model):
    long_url = models.CharField(max_length=255)
    short_url= models.CharField(max_length=6)

    def __str__(self):
        return self.long_url

