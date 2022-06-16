from django.db import models


class Urlshort(models.Model):
    ourl: models.URLField()
    surl: models.TextField(max_length=51)
    num_clicked: models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.surl + '=' + (self.ourl)
# Create your models here.
