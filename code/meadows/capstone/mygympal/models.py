from django.db import models
from django.contrib.auth import get_user_model

class Blog(models.Model):
    title = models.CharField(max_length=200)
    username = models.ForeignKey(get_user_model(), related_name='posts', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    body = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']