from django.db import models

class URLShortener(models.Model):

    taken_url = models.URLField(max_length=500)

    given_url = models.CharField(max_length=15, unique=True, blank=True)

    def __str__(self):
        return f'{self.taken_url} to {self.given_url}'

