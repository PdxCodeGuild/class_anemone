from django.db import models

class ShortURL(models.Model):

    long_url = models.URLField()

    short_url = models.CharField(max_length=10, unique=True, blank=True)

    def __str__(self):
        return self.long_url, self.short_url
