from django.db import models
from django.urls import reverse

# Create your models here.

class Twiddle(models.Model):
    twidd = models.CharField(max_length= 255)
    twiddler = models.ForeignKey('auth.User',max_length=200, related_name="twiddles",on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    twiddle = models.TextField(max_length=10000)
    
    def __str__(self):
        return self.twidd
    
    def get_absolute_url(self):
        return reverse('posts:detail', args=(self.pk,))

    class Meta:
        ordering = ['-created_date']