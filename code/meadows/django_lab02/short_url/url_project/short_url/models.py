from django.db import models

class ShortUrl(models.Model):
    created = models.DateTimeField()
    long_url = models.URLField()
    small_url = models.CharField(max_length=8, unique=True, blank=True)

    def __str__(self):
        self.long_url + '-' + self.small_url