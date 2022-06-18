from django.db import models
from random import choice
from string import ascii_letters, digits

class Shurl(models.Model):

    long_url = models.URLField(max_length=200)

    short_url = models.CharField(max_length=10, unique=True, blank=True)

    def random_code(self):
        chars = ascii_letters + digits
        return "".join([choice(chars) for _ in range(6)])

    def shorten_url(self):
        new_url = self.random_code()
        if Shurl.objects.filter(short_url=new_url).exists():
            return self.shorten_url()
        return new_url

    def __str__(self):
        return f'{self.long_url} - {self.short_url}'

    

    

