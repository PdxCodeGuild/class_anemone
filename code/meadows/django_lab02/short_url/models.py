from django.db import models
from string import ascii_letters, digits
import random

class ShortUrl(models.Model):
    long_url = models.URLField()
    small_url = models.CharField(max_length=5, primary_key=True, editable=False)
    # pub_date = models.DateTimeField(verbose_name='date')

    def __str__(self):
        self.small_url
    
    def snipped(self):
        self.small_url = ''.join(random.choice(ascii_letters+digits)for x in range (5))