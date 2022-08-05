
from django.db import models

# Create your models here.
class Input(models.Model):
    address = models.CharField(max_length=120)
    city = models.CharField(max_length = 40)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)

    def __str__(self):
        return self.address