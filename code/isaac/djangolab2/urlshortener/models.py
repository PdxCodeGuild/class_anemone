from django.db import models

# Create your models here.

class UrlShort(models.Model):
    # Create a field that accepts url input
    url = models.URLField()
    code = models.CharField(max_length=6)

    def __str__(self):
        return f"{self.url}-{self.code}"
