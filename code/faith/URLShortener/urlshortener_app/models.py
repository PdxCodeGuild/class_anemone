from django.db import models

# Create your models here.
class URLShort(models.Model):
    long_url = models.URLField(max_length=400)
    short_url = models.CharField(max_length=20)


    def __str__(self):
        return self.short_url