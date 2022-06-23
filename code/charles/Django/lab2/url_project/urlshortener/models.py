from django.db import models


class Urlshort(models.Model):
    ourl = models.URLField(max_length=300)
    surl = models.CharField(max_length=51)
    num_clicked = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.surl + ' goes to ' + self.ourl
# Create your models here.
