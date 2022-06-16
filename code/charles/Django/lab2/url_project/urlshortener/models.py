from django.db import models


class Urlshort(models.Model):
    ourl: models.TextField(max_length=300)
    surl: models.TextField(max_lenth=51)

    def __str__(self):
        return surl + '=' + (ourl)
# Create your models here.
