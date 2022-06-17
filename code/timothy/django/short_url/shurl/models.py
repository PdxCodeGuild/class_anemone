from django.db import models
from utils import shortener

class Shortener(models.Model):

    long_url = models.URLField(max_length=200)

    created = models.DateTimeField(auto_now_add=True)

    short_url = models.CharField(max_length=20, unique=True, blank=True)

    class Meta:
        order = ["-created"]

    def __str__(self):
        return f'{self.long_url} - {self.short_url}'

    def save(self, *args, **kwargs):

        if not self.short_url:
            self.short_url = shortener(self)

        super().save(*args, **kwargs)

    