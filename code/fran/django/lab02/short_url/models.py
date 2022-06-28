from django.db import models

class ShortUrlCode(models.Model):
    code = models.CharField(max_length=6)
    url = models.CharField(max_length=1000)
    create_date = models.DateTimeField()

    # customize the string representation for the ShortUrlCode object
    def __str__(self):
        return self.code
