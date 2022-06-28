from django.db import models

# Create your models here.

class UrlChoppa(models.Model):
    url = models.CharField(max_length=255)
    pub_date = models.DateTimeField(verbose_name="date published")
    url_code = models.CharField(max_length=6)
    ip_addy = models.CharField(max_length=50)
    def __str__(self):
        return self.url_code
    
