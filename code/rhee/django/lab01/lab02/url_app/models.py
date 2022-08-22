from django.db import models

# Create your models here.
class ShortURL(models.Model):
    old_url = models.URLField(max_length=10000)
    new_url = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.old_url}  - {self.new_url}"